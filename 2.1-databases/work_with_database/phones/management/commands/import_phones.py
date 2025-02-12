
import csv
from django.core.management.base import BaseCommand
from phones.models import Phone
from django.utils.text import slugify
from datetime import datetime


class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = csv.DictReader(file, delimiter=';')

            for phone in phones:
                Phone.objects.create(
                    name=phone['name'],
                    price=float(phone['price']),
                    image=phone['image'],
                    release_date=datetime.strptime(phone['release_date'], '%Y-%m-%d').date(),
                    lte_exists=phone['lte_exists'].lower() in ('true', '1'),
                    slug=slugify(phone['name'])
                )

        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))
