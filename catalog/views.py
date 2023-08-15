from linecache import cache

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView
from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from config import settings


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'

    # def get_queryset(self):
    #    queryset = super().get_queryset()
    #    active_versions = Version.objects.filter(current_version=True)
    #    active_product_ids = active_versions.values_list('product__id', flat=True)
    #    queryset = queryset.filter(id__in=active_product_ids)
    #    return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    login_url = 'user:login'

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product')
    login_url = 'user:login'

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


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    permission_required = 'catalog.view_product'


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product')
    login_url = 'user:login'


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
def edit_product(request, product_id):
    # Получение продукта по идентификатору
    product = get_object_or_404(Product, id=product_id)

    if product.owner == request.user:
        # Проверка, что текущий пользователь является владельцем продукта
        # Обработка случая, когда пользователь пытается изменить чужой продукт
        return redirect('product_list')

    if request.method != 'POST':
        # Отображение формы редактирования продукта
        return render(request, 'user/edit_product.html', {'product': product})
    form = UserCreationForm(request.POST)
    if form.is_valid():
        pass
    return redirect('product_list')


def get_category_data():
    if settings.CACHE_ENABLED:
        key = 'category_list'
        category_list = cache.get(key)
        if category_list is None:
            print('No category cache detected. I gonna cache it')
            category_list = Category.objects.all()
            cache.set(key, category_list)
    else:
        category_list = Category.objects.all()
    return category_list


class CategoryView(ListView):
    model = Category

    def get_queryset(self, *args, **kwargs):
        return get_category_data()
