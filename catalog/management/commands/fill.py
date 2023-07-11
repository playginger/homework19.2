from django.core.management import BaseCommand

from catalog.models import Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_create = [
            {'product_name': 'ПК', 'product_description': 'Игровые, мощные, бомбические ПК',
             'category': 2, 'product_prise': 123000},
            {'product_name': 'Звук', 'product_description': 'Крутая стереосистема, соседи будут не рады',
             'category': 1, 'product_prise': 50000},
            {'product_name': 'Микрофоны', 'product_description': 'Для качественного стриминга, нужно пара микрофонов',
             'category': 1, 'product_prise': 7000},
            {'product_name': 'Мониторы', 'product_description': 'Что бы видеть каждую морщинку, каждый пиксель,'
                                                                ' каждую пищинку, ну вы поняли ',
             'category': 2, 'product_prise': 15000},
            {'product_name': 'Клавиатура и мышь', 'product_description': 'Что бы ваши пальчики были в тонусе,'
                                                                         ' и в сложных катках вы были MVP',
             'category': 2, 'product_prise': 123000}
        ]

        product_for_create = []
        for product in product_create:
            product_for_create.append(Product(**product))

        print(product_for_create)

        Product.objects.bulk_create(product_for_create)