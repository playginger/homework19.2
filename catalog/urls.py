from django.urls import path
from catalog.views import home
from . import views

urlpatterns = [
    path('', home),
    path('contacts/', views.contacts, name='contacts')
]
