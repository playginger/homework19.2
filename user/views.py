from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from catalog.models import Product
from user.forms import RegisterForm
from user.models import User


class UserProfileView(UpdateView):
    model = User
    form_class = UserChangeForm

    def form_valid(self, form):
        # Метод, который отрабатывает при успешной валидации формы
        if form.is_valid():
            self.object = form.save()
            # Сохранение объекта перед тем, как установить ему пароль
            if form.data.get('need_generate', False):
                pas = self.object.make_random_password(12)
                self.object.set_passeword(  # Функция установки пароля,
                    # которая хэширует строку для того,
                    # чтобы не хранить пароль в открытом виде в БД
                    pas  # Функция генерации пароля
                )

                # send mail ()

                self.object.save()

        return super().form_valid(form)


class RegisterView(CreateView):
    # Создаем обычный контроллер на создание сущности
    model = User
    form_class = RegisterForm
    success_url = reverse_lazy('user:user_registr')


class LogoutView(BaseLogoutView):
    pass


Users = get_user_model()


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Генерация уникального токена верификации и отправка письма
            import uuid

            token = str(uuid.uuid4())
            user.token = token
            # user.со[ранить

            st = f"pereidei po URL   http://localhost:8000/verify_email/?token={token}"
            return redirect('verification_sent')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def verify_email(request):
    token = request.GET.get('token')
    try:
        user = User.objects.get(email_verification_token=token)
    except User.DoesNotExist:
        return redirect('invalid_token')

    user.is_email_verified = True
    user.is_active = True
    user.save()
    login(request, user)
    return redirect('/')


@login_required
def home(request):
    return render(request, 'home.html')
