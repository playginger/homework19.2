from django.urls import path
from . import views
from .apps import UserConfig
from .views import LogoutView

app_name = UserConfig.name


urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('verify-email/', views.verify_email, name='verify_email'),
    path('home/', views.home, name='home'),
    path('logout', LogoutView.as_view(), name='logout')
]