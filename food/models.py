from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
