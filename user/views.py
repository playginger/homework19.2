from django.contrib.auth import get_user_model, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.views import LogoutView as BaseLogoutView, LoginView

from config import settings
from user.email_verification_token_generator import email_verification_token
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

    model = User
    form_class = RegisterForm

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        current_site = get_current_site(self.request)
        subject = 'Активация профиля'

        send_mail(
            subject=subject,
            message=f'Активируйте ваш профиль: http://{current_site.domain}/user/activate/{urlsafe_base64_encode(force_bytes(new_user.pk))}/{email_verification_token.make_token(new_user)}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)

    success_url = reverse_lazy('user:login')
    template_name = 'user/register.html'


class ActivateView(View):

    def get_user_from_email_verification_token(self, uid, token: str):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = get_user_model().objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError,
                get_user_model().DoesNotExist):
            return None

        if user is not None \
                and \
                email_verification_token.check_token(user, token):
            return user
        return None

    def get(self, request, uidb64, token):
        user = self.get_user_from_email_verification_token(uidb64, token)
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('user:login')


class LogoutView(BaseLogoutView):
    pass


class UserLoginView(LoginView):
    template_name = 'user/login.html'


# Users = get_user_model()


# def register(request):
# if request.method == 'POST':
#     form = UserCreationForm(request.POST)
#    if form.is_valid():
##         user = form.save()
# Генерация уникального токена верификации и отправка письма

##         token = str(uuid.uuid4())
##         user.token = token
# user.save

##         st = f"pereidei po URL   http://localhost:8000/verify_email/?token={token}"
##         return redirect('verification_sent')
## else:
##     form = UserCreationForm()
## return render(request, 'user/register.html', {'form': form})


# def verify_email(request):
# token = request.GET.get('token')
# try:
#     user = User.objects.get(email_verification_token=token)
# except User.DoesNotExist:
#     return redirect('invalid_token')

# user.is_email_verified = True
# user.is_active = True
# user.save()
# login(request, user)
# return redirect('/')


@login_required
def home(request):
    return render(request, 'user/home.html')
