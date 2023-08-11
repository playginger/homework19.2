from django.contrib.auth.forms import UserCreationForm

from user.models import User


class RegisterForm(UserCreationForm):
    # Наследуемся от специальной формы UserCreationForm из модуля auth
    class Meta:
        model = User
        # Указываем новую кастомную модель
        fields = ('email', 'password1', 'password2',)
