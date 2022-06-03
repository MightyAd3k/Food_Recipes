from datetime import datetime
import random

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from food.models import Recipe, Plan


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
        all_plans = Plan.objects.all().count()
        last_added_plan = Plan.objects.last()
        ctx = {
            'all_recipes': all_recipes,
            'all_plans': all_plans,
            'last_added_plan': last_added_plan
        }
        return render(request, 'dashboard.html', ctx)


class RecipeList(View):

    def get(self, request):
        recipes_list = Recipe.objects.all().order_by('-votes', '-created')
        paginator = Paginator(recipes_list, 30)

        page = request.GET.get('page')
        recipes = paginator.get_page(page)

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
        plans = Plan.objects.all()
        ctx = {'plans': plans}
        return render(request, "app-schedules.html", ctx)
