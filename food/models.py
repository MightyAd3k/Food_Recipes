from django.db import models
from django.urls import reverse


class Recipe(models.Model):
    name = models.CharField(max_length=200, null=False)
    ingredients = models.TextField()
    description = models.TextField()
    preparation = models.TextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    preparation_time = models.IntegerField(help_text='Time in minutes')
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'

    def ingredients_as_list(self):
        return self.ingredients.split(',')


class Plan(models.Model):
    name = models.CharField(max_length=30, null=False)
    description = models.TextField()
    created = models.DateTimeField(auto_now=True, null=True, blank=True)
    recipes = models.ManyToManyField(Recipe, through='RecipePlan')

    def __str__(self):
        return f'{self.name} {self.description}'


class NameOfTheDay(models.Model):
    name = models.CharField(max_length=10)
    order = models.IntegerField(unique=True)

    def __str__(self):
        return f'{self.name}'


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=25)
    order = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    day_name = models.ForeignKey(NameOfTheDay, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.meal_name} {self.order} {self.recipe} {self.day_name}'
