from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=40)
    description = models.CharField(max_length=300)
    preparation = models.CharField(max_length=500)
    created = models.DateField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    preparation_time = models.IntegerField()
    votes = models.IntegerField(default=0)

    def ingredients_as_list(self):
        return self.ingredients.split()


class Plan(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True, null=True, blank=True)
    recipes = models.ManyToManyField(Recipe)


class DayName(models.Model):
    name = models.CharField(max_length=10)
    order = models.IntegerField(unique=True)


class RecipePlan(models.Model):
    meal_name = models.CharField(max_length=10)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    order = models.IntegerField()
    day_name = models.ForeignKey(DayName, on_delete=models.CASCADE)
