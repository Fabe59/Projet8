from django.core.management.base import BaseCommand, CommandError

from food.off import Database

class Command(BaseCommand):

    def handle(self, *args, **options):
        db = Database()
        db.insert_cat_in_db()
