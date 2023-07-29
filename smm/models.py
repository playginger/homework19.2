from django.db import models


NULLABLE = {'blank': True, 'null': True}


class ServiceClient(models.Model):
    email = models.EmailField(max_length=254, verbose_name='Email', unique=True),
    fullname = models.CharField(max_length=500, verbose_name='ФИО'),
    comment = models.TextField(max_length=1000, verbose_name='Комментарий', **NULLABLE),

    def __str__(self):
        return f"{self.fullname} ({self.email})"


    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'



class Newsletter(models.Model):
    mailing_time = models.TimeField(verbose_name='время рассылки'),
    frequency = models.CharField(max_length=100, choices=[
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц')
    ])
    mailing_status = models.CharField(max_length=100, choices=[
        ('established', 'создана'),
        ('launched', 'запущена'),
        ('completed', 'завершена'),
    ])
    client = models.ForeignKey(ServiceClient, on_delete=models.CASCADE, verbose_name='клиент'),

    def __str__(self):
        return f"Настройки рассылки - {self.frequency} ({self.mailing_time}{self.mailing_status})"

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'

class Message(models.Model):
    letter_subject = models.CharField(max_length=100, verbose_name='тема письма'),
    letter_body = models.TextField(max_length=1000, verbose_name='тело письма', **NULLABLE),

    def __str__(self):
        return f"Настройки письма - {self.letter_subject}"

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'

class Mailinglogs(models.Model):
    last_attempt = models.DateTimeField(auto_now_add=True, verbose_name='дата и время последней попытки'),
    attempt_status = models.BooleanField(default=True),
    mail_server = models.CharField(max_length=100, verbose_name='сервер',**NULLABLE),

    def __str__(self):
        return f"Cообщение от {self.last_attempt}"

    class Meta:
        verbose_name = 'лог'
        verbose_name_plural = 'логи'
