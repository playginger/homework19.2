# Generated by Django 4.0.4 on 2023-07-31 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_alter_product_product_prise_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_prise_name',
            field=models.CharField(max_length=100, verbose_name='необязательное поле'),
        ),
    ]