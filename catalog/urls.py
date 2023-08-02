from django.urls import path
from catalog.views import ProductListView, CategoryListView, ProductCreateView, ProductUpdateView
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('index/', CategoryListView.as_view(), name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product')
]
