from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from catalog.forms import ProductForm
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

class ProductDeleteView(DeleteView):
    model = Product
    form_class = ProductForm
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
