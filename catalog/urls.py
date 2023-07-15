from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from catalog.views import home, index, product, category_product
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('product/', product, name='product'),
    path('<int:pk>/product/', category_product, name='category_product'),
    path('', home),
    path('contacts/', views.contacts, name='contacts')
]
