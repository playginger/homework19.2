# Generated by Django 4.0.4 on 2023-08-17 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100, verbose_name='наименование')),
                ('category_description', models.CharField(max_length=100, verbose_name='описание')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
                'ordering': ('category_name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='наименование')),
                ('product_description', models.CharField(max_length=100, verbose_name='описание')),
                ('img', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('product_prise', models.IntegerField(default=0, verbose_name='Цена')),
                ('product_prise_name', models.CharField(max_length=100, verbose_name='необязательное поле')),
                ('product_date', models.DateTimeField(auto_now_add=True)),
                ('product_last', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
                'ordering': ('product_name',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.CharField(max_length=50)),
                ('version_name', models.CharField(max_length=100)),
                ('current_version', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.product')),
            ],
            options={
                'verbose_name': 'версия',
                'verbose_name_plural': 'версии',
                'ordering': ('version_number',),
            },
        ),
    ]
