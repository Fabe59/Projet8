from food.constants import CATEGORIES_LIST, OFF_API_URL
from food.models import Category, Product
import requests

class Database:

    def get_categories(self):
        for cat in CATEGORIES_LIST:
            Category.objects.create(name=cat)         
    
    def get_products(self):
        for cat in CATEGORIES_LIST:
            params = {
                "action": "process",
                "tagtype_0": "categories",
                "tag_contains_0": "contains",
                "tag_0": cat,
                "page_size": 10,
                "json": 1
                }
            response = requests.get(OFF_API_URL, params=params)
            data = response.json()

            for product in data['products']:
                brand = product.get('brands')
                product_name = product.get('product_name_fr')
                nutriscore = product.get('nutrition_grade_fr')
                url = product.get('url')
                image_url = product.get('image_front_url')

                prod = Product(brand=brand, name=product_name, nutrition_grade_fr=nutriscore, url=url, image_url=image_url)
                prod.save()
                for category in CATEGORIES_LIST:
                    category, _ = Category.objects.get_or_create(name=category)
                    prod.category.add(category)