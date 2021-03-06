from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200, null=False)
    ingredients = models.TextField()
    description = models.TextField()
    preparation = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField(help_text="Time in minutes")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    def ingredients_as_list(self):
        return self.ingredients.split(",")


class Vote(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Plan(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe, through="RecipePlan")

    def __str__(self):
        return f'{self.name}'


class NameOfTheDay(models.Model):
    name = models.CharField(max_length=10)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.name}"


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=25)
    order = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    day_name = models.ForeignKey(NameOfTheDay, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meal_name} {self.order} {self.recipe} {self.day_name}'


class Page(models.Model):
    title = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField()
    slug = models.SlugField(max_length=100)
