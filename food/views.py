from datetime import datetime
import random

from django.shortcuts import render
from django.views import View

from food.models import Recipe


# class IndexView(View):
#
#     def get(self, request):
#         ctx = {"actual_date": datetime.now()}
#         return render(request, "test.html", ctx)


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


class Dashboard(View):

    def get(self, request):
        all_recipes = Recipe.objects.all().count()
        #all_plans = Plan.objects.all().count()
        ctx = {
            'all_recipes': all_recipes,
            #'all_plans': all_plans
        }
        return render(request, 'dashboard.html', ctx)


class RecipeList(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        ctx = {'recipes': recipes}
        return render(request, "app-recipes.html", ctx)


class AddRecipe(View):

    def get(self, request):
        return render(request, "app-add-recipe.html")


class ModifyRecipe(View):

    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        ctx = {'recipe': recipe}
        return render(request, "app-recipe-details.html", ctx)

    def post(self, request, pk):
        pass



class PlanList(View):

    def get(self, request):
        # plans = Plan.objects.all()
        # ctx = {'plans': plans}
        return render(request, "app-schedules.html")
