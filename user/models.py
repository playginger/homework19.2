from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    img = models.ImageField(verbose_name='аватар', **NULLABLE)
    phone_number = models.CharField(max_length=20, verbose_name='телефон')
    country = models.CharField(max_length=20, verbose_name='страна')
    email = models.EmailField(verbose_name='почта', unique=True)
    email_verification_token = models.CharField(max_length=255, null=True, blank=True)
    is_email_verified = models.BooleanField(default=False)
    fullname = models.CharField(max_length=500, verbose_name='ФИО'),
    comment = models.TextField(max_length=1000, verbose_name='Комментарий', **NULLABLE),

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone_number} {self.country}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
