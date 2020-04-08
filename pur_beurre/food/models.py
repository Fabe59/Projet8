from django.db import models

# Create your models here.

class Category(models.Model):
    """To create the Category table in the database"""
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
