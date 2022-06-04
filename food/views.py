from datetime import datetime
import random

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView

from food.models import Recipe, Plan, RecipePlan


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

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')
        preparation_time = request.POST.get('preparation_time')
        preparation = request.POST.get('preparation')
        ingredients = request.POST.get('ingredients')

        if Recipe.objects.filter(name=name).exists():
            return render(request, "app-add-recipe.html", {'error': 'Przepis o tej nazwie już istnieje'})

        if not name or description or preparation_time or preparation or ingredients:
            return render(request, "app-add-recipe.html", {'error1': 'Wypełnij wszystkie pola'})

        Recipe.objects.create(name=name,
                              description=description,
                              preparation_time=preparation_time,
                              preparation=preparation,
                              ingredients=ingredients,
                              )

        return redirect('recipes')


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


class PlanDetailView(View):

    def get(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        lst_recipes = []
        for i in range(7):
            lst_recipes.append(RecipePlan.objects.filter(plan_id__exact=pk, day_name_id__exact=i+1))

        ctx = {
            'plan': plan,
            'days': lst_recipes
        }
        return render(request, 'app-details-schedules.html', ctx)


# class RecipePlanDetailView(DetailView):
#     model = RecipePlan
#     template_name = 'app-details-schedules.html'
