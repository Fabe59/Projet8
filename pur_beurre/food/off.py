from food.constants import CATEGORIES_LIST, OFF_API_URL
from food.models import Category, Product
import requests

class Database:

    def insert_cat_in_db(self):
        for cat in CATEGORIES_LIST:
            Category.objects.create(name=cat)
    
    def get_products(self):
        for cat in CATEGORIES_LIST:
            params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cat,
                "page_size": 500,
                "json": 1
                }
            response = requests.get(OFF_API_URL, params=params)
            data = response.json()

        for product in data['products']:
            brand = product.get('brands')
            if name is None:
                continue
            product_name = product.get('product_name_fr')
            if product_name is None:
                continue
            nutriscore = product.get('nutrition_grade_fr')
            if nutriscore is None:
                continue
            url = product.get('url')
            if url is None:
                continue
            image_url = product.get('image_front_url')
            if image_url is None:
                continue

            prod = Product(brand=brand, name=product_name, nutrition_grade_fr=nutriscore, url=url, image_url=image_url)
            prod.save()
