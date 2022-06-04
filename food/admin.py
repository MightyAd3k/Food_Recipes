from django.contrib import admin

from food.models import Recipe, Plan, NameOfTheDay, RecipePlan


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ingredients', 'description', 'created']


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created']


@admin.register(NameOfTheDay)
class NameOfTheDayAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']


@admin.register(RecipePlan)
class RecipePlanAdmin(admin.ModelAdmin):
    list_display = ['meal_name', 'order', 'day_name']
