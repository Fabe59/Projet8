from django.db import models

# Create your models here.

class Category(models.Model):
    """To create the Category table in the database"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    """To create the Product table in the database"""
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    nutrition_grade_fr = models.CharField(max_length=1)
    url = models.URLField(max_length=250)
    image_url = models.URLField(max_length=250)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)