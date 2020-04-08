from food.constants import CATEGORIES_LIST
from food.models import Category

class Database:

    def insert_cat_in_db(self):
        for cat in CATEGORIES_LIST:
            Category.objects.create(name=cat)