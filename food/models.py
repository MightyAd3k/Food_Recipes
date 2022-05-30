from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=40)
    description = models.CharField(max_length=255)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)
