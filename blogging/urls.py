from django.urls import path
from django.views.decorators.cache import cache_page

from blogging.apps import BloggingConfig
from blogging.views import BloggingListView, BloggingCreateView, BloggingDetailView, BloggingUpdateView, \
    BloggingDeleteView

app_name = BloggingConfig.name

urlpatterns = [
    path('', cache_page(60)(BloggingListView.as_view()), name='list'),
    path('blogging_create/', BloggingCreateView.as_view(), name='create'),
    path('blogging_detail/<int:pk>/', BloggingDetailView.as_view(), name='detail'),
    path('blogging_update/<int:pk>/', BloggingUpdateView.as_view(), name='update'),
    path('blogging_delete/<int:pk>/', BloggingDeleteView.as_view(), name='delete'),
]
