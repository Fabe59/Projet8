from django.core.management.base import BaseCommand
from food.off import Database


class Command(BaseCommand):

    def handle(self, *args, **options):
        dbupdate = Database()
        dbupdate.get_products()