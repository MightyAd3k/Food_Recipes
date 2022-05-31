from django.contrib import admin

from food.models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'ingredients', 'description', 'created']
