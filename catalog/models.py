from django.db import models

from user.models import User

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.CharField(max_length=100, verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.CharField(max_length=100, verbose_name='описание')
    img = models.ImageField(verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_prise = models.IntegerField(default=0, verbose_name='Цена')
    product_prise_name = models.CharField(max_length=100, verbose_name='необязательное поле')
    product_date = models.DateTimeField(auto_now_add=True)
    product_last = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.product_name} {self.product_description}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Version(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    version_number = models.CharField(max_length=50)
    version_name = models.CharField(max_length=100)
    current_version = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product} {self.version_number} {self.current_version}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('version_number',)
