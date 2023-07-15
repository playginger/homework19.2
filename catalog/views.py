from django.shortcuts import render


from catalog.models import Category, Product


def index(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'PowerPC Shop'
    }
    return render(request, 'catalog/index.html', context)


def product(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары'
    }
    return render(request, 'catalog/product.html', context)


def category_product(request, pk):
    category_item = Category.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category_id=pk),
        'title': 'Товары'
    }
    return render(request, 'catalog/product.html', context)

def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name} ({phone}) {message}')
    return render(request, 'catalog/contacts.html')

