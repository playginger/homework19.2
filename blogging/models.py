from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Blogging(models.Model):
    header = models.CharField(max_length=100, verbose_name='заголовок')
    slug = models.CharField(max_length=100, verbose_name='ссылка')
    content = models.TextField(max_length=500, verbose_name='текст')
    img = models.ImageField(verbose_name='превью', **NULLABLE)
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    publications = models.BooleanField(default=True, verbose_name='публикации')
    views = models.IntegerField(default=0, verbose_name='количество просмотров')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = 'заголовок'
        verbose_name_plural = 'заголовки'
        ordering = ('header',)
