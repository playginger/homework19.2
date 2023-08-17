from time import sleep

from django.core.management import BaseCommand

from catalog.models import Product, Category
from smm.models import Newsletter


class Command(BaseCommand):

    def handle(self, *args, **options):
        news = Newsletter.objects.all()

        for new in news:
            last = new.logs.all().order_by('-last_attempt').first()
            if  last.last_attempt + new.frequency > today():
                send()

            sleep(5)

