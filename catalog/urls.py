from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import ProductListView, CategoryListView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductDetailView
from . import views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product'),
    path('index/', CategoryListView.as_view(), name='index'),
    path('contacts/', views.contacts, name='contacts'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('edit-product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('catalog/<int:page>/', cache_page(60)(ProductListView.as_view()), name='detail_category'),
]
