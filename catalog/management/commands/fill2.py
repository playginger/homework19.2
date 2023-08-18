from time import sleep
from django.core.management.base import BaseCommand
from smm.models import Newsletter
from datetime import datetime, timedelta


class Command(BaseCommand):
    def handle(self, *args, **options):
        news = Newsletter.objects.all()
        today = datetime.now().date()
        for new in news:
            last = new.logs.all().order_by('-last_attempt').first()
            if last and last.last_attempt.date() + timedelta(days=new.frequency) > today:
                send(new)
            sleep(5)


def send(newsletter):
    print(f"Отправка рассылки для {newsletter}")
