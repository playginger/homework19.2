from django.urls import path
from blogging.apps import BloggingConfig
from blogging.views import BloggingListView, BloggingCreateView, BloggingDetailView, BloggingUpdateView, \
    BloggingDeleteView

app_name = BloggingConfig.name

urlpatterns = [
    path('blogging_list/', BloggingListView.as_view(), name='list'),
    path('blogging_detail/<int:pk>/', BloggingDetailView.as_view(), name='detail'),
    path('blogging_create/', BloggingCreateView.as_view(), name='create'),
    path('blogging_update/<int:pk>/', BloggingUpdateView.as_view(), name='update'),
    path('blogging_delete/<int:pk>/', BloggingDeleteView.as_view(), name='delete'),
]
