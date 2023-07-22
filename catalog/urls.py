from django.urls import path
from catalog.views import home, ProductListView
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('',ProductListView.as_view(), name='product'),
    #path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('', home),
    path('contacts/', views.contacts, name='contacts')
]
