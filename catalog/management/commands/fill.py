from time import sleep

from django.core.management import BaseCommand

from catalog.models import Product, Category
from smm.models import Newsletter


class Command(BaseCommand):

    def handle(self, *args, **options):

        category_create = [{
            'category_name': 'железо ПК', 'category_description': 'комплектующие'},
            {'category_name': 'Допы к ПК', 'category_description': 'всякое'

             }]

        category_for_create = []
        for category in category_create:
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        product_create = [
            {'product_name': 'Cистемные блоки', 'product_description': 'Игровые, мощные, бомбические ПК',
             'category': category_for_create[1], 'product_prise_name': 'от', 'product_prise': 75000},
            {'product_name': 'Звук', 'product_description': 'Крутая стереосистема, соседи будут не рады',
             'category': category_for_create[0], 'product_prise_name': 'от', 'product_prise': 50000},
            {'product_name': 'Микрофоны', 'product_description': 'Для качественного стриминга, нужно пара микрофонов',
             'category': category_for_create[0], 'product_prise_name': 'от', 'product_prise': 7000},
            {'product_name': 'Мониторы', 'product_description': 'Что бы видеть каждую морщинку, каждый пиксель,'
                                                                ' каждую пищинку, ну вы поняли ',
             'category': category_for_create[1], 'product_prise_name': 'от', 'product_prise': 15000},
            {'product_name': 'Клавиатура и мышь', 'product_description': 'Что бы ваши пальчики были в тонусе,'
                                                                         ' и в сложных катках вы были MVP',
             'category': category_for_create[1], 'product_prise_name': 'от', 'product_prise': 5000}
        ]

        product_for_create = []
        for product in product_create:
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)
