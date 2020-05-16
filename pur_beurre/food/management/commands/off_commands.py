from django.core.management.base import BaseCommand
from food.off import Database


class Command(BaseCommand):

    def handle(self, *args, **options):
        db = Database()
        db.get_categories()
        db.get_products()
