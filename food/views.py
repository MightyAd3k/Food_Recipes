from datetime import datetime
import random

from django.shortcuts import render
from django.views import View

from food.models import Recipe


class IndexView(View):

    def get(self, request):
        ctx = {"actual_date": datetime.now()}
        return render(request, "test.html", ctx)


class LandingPage(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        three_random_recipes = list(range(0, recipes.count()))
        random.shuffle(three_random_recipes)
        ctx = {
            'recipe1': recipes[three_random_recipes[0]],
            'recipe2': recipes[three_random_recipes[1]],
            'recipe3': recipes[three_random_recipes[2]]
        }
        return render(request, "index.html", ctx)


class Recipes(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        ctx = {'recipes': recipes}
        return render(request, "app-recipes.html", ctx)
