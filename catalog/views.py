from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'

    #def get_queryset(self):
    #    queryset = super().get_queryset()
    #    active_versions = Version.objects.filter(current_version=True)
    #    active_product_ids = active_versions.values_list('product__id', flat=True)
    #    queryset = queryset.filter(id__in=active_product_ids)
    #    return queryset

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Product



class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')


class CategoryListView(ListView):
    model = Product
    template_name = 'catalog/index.html'

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html')


@login_required
def create_product(request):
    if request.method == 'POST':
        # Создание продукта с текущим пользователем в качестве владельца

        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()

            product.owner = request.user
            product.save()

        return redirect('product_list')
    else:
        # Отображение формы создания продукта
        return render(request, 'create_product.html')


@login_required
def edit_product(request, product_id):
    # Получение продукта по идентификатору
    product = get_object_or_404(Product, id=product_id)

    if product.owner != request.user:
        # Проверка, что текущий пользователь является владельцем продукта
        # Обработка случая, когда пользователь пытается изменить чужой продукт
        return redirect('product_list')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          pass
        return redirect('product_list')
    else:
        # Отображение формы редактирования продукта
        return render(request, 'edit_product.html', {'product': product})

