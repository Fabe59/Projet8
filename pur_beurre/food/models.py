from django.db import models

# Create your models here.

class Category(models.Model):
    """To create the Category table in the database"""
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Product(models.Model):
    """To create the Product table in the database"""
    brand = models.CharField(max_length=250, blank=True, null=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    nutrition_grade_fr = models.CharField(max_length=1, blank=True, null=True)
    stores = models.TextField(max_length=400, blank=True, null=True)
    url = models.URLField(max_length=250, blank=True, null=True)
    image_url = models.URLField(max_length=250, blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return '{} {}'.format(self.brand, self.name)