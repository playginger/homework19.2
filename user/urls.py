from django.urls import path
from . import views
from .apps import UserConfig
from .views import LogoutView, ActivateView, RegisterView, UserLoginView

app_name = UserConfig.name


urlpatterns = [
    path('profile/<int:pk>/', views.UserProfileView.as_view(), name='profile'),
    path('register/', RegisterView.as_view(), name='register'),
    path('home/', views.home, name='home'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('activate/<uidb64>/<token>', ActivateView.as_view(), name='activate'),
    path('', UserLoginView.as_view(), name='login'),
]