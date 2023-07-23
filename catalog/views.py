from django.shortcuts import render
from django.views.generic import ListView, DetailView

from catalog.models import Product


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product.html'


class CategoryListView(ListView):
    model = Product
    template_name = 'catalog/index.html'


# class ProductDetailView(DetailView):
#    model = Product
#    template_name = 'catalog/product.html'
#    context_object_name = 'product'


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html')
