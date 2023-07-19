from django.urls import path
from catalog.views import home, ProductListView, ProductDetailView
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('',ProductListView.as_view(), name='index'),
    path('product/', ProductDetailView.as_view(), name='product'),
    path('', home),
    path('contacts/', views.contacts, name='contacts')
]
