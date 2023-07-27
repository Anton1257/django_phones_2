import csv

from django.core.management.base import BaseCommand
from app.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("полный/путь/до/файла/phones.csv", "r") as file:
            reader = list(csv.DictReader(file, delimiter=";"))
        for row in reader:
            Phone.objects.create(
                name=row["name"],
                price=row["price"],
                image=row["image"],
                release_date=row["release_date"],
                lte_exists=row["lte_exists"],
            )
