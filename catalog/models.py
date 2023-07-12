from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='наименование')
    category_description = models.CharField(max_length=100, verbose_name='описание')

    def __str__(self):
        return f'{self.category_name} {self.category_description}'

    class Meta:
        verbose_name = 'наименование'
        verbose_name_plural = 'наименования'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование')
    product_description = models.CharField(max_length=100, verbose_name='описание')
    img = models.ImageField(upload_to='preview/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    product_prise = models.IntegerField(default=0, verbose_name='наименование')
    product_date = models.DateTimeField(auto_now_add=True)
    product_last = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.product_name} {self.product_description}'

    class Meta:
        verbose_name = 'наименование'
        verbose_name_plural = 'наименования'
        ordering = ('product_name',)
