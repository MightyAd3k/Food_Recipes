import random

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View

from food.models import Recipe, Plan, RecipePlan, NameOfTheDay, Page


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

        lst_days = []
        for i in range(7):
            lst_days.append(RecipePlan.objects.filter(plan_id=last_added_plan, day_name_id=i + 1))

        ctx = {
            'all_recipes': all_recipes,
            'all_plans': all_plans,
            'last_added_plan': last_added_plan,
            'days': lst_days
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


class RecipeDetails(View):

    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        ctx = {'recipe': recipe}
        return render(request, "app-recipe-details.html", ctx)

    def post(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)

        if 'like' in request.POST:
            recipe.votes += 1
            recipe.save()

        else:
            recipe.votes -= 1
            recipe.save()

        ctx = {'recipe': recipe}
        return render(request, "app-recipe-details.html", ctx)


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

        if name == '' or description == '' or preparation_time == '' or preparation == '' or ingredients == '':
            return render(request, "app-add-recipe.html", {'error1': 'Wypełnij wszystkie pola'})

        Recipe.objects.create(name=name,
                              description=description,
                              preparation_time=preparation_time,
                              preparation=preparation,
                              ingredients=ingredients,
                              )

        return redirect('recipes')


class UpdateRecipe(View):

    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        ctx = {'recipe': recipe}
        return render(request, "app-edit-recipe.html", ctx)

    def post(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        name = request.POST.get('name')
        description = request.POST.get('description')
        preparation_time = request.POST.get('preparation_time')
        preparation = request.POST.get('preparation')
        ingredients = request.POST.get('ingredients')

        if name != recipe.name and Recipe.objects.filter(name=name).first():
            return render(request, "app-edit-recipe.html", {'recipe': recipe, 'error': 'Przepis o tej nazwie już istnieje'})

        if description == '' or preparation_time == '' or preparation == '' or ingredients == '':
            return render(request, "app-edit-recipe.html", {'recipe': recipe, 'error1': 'Wypełnij wszystkie pola'})

        recipe.name = name
        recipe.description = description
        recipe.preparation_time = preparation_time
        recipe.preparation = preparation
        recipe.ingredients = ingredients
        recipe.save()

        return redirect('recipes')


class DeleteRecipe(View):

    def get(self, request, pk):
        recipe = Recipe.objects.get(pk=pk)
        recipe.delete()
        return redirect('recipes')


class PlanList(View):

    def get(self, request):
        plans_list = Plan.objects.all().order_by('name')
        paginator = Paginator(plans_list, 30)

        page = request.GET.get('page')
        plans = paginator.get_page(page)

        ctx = {'plans': plans}
        return render(request, "app-schedules.html", ctx)


class PlanDetails(View):

    def get(self, request, pk):
        plan = Plan.objects.get(pk=pk)
        lst_days = []
        for i in range(7):
            lst_days.append(RecipePlan.objects.filter(plan_id=pk, day_name_id=i + 1))

        ctx = {
            'plan': plan,
            'days': lst_days
        }
        return render(request, 'app-details-schedules.html', ctx)


class AddPlan(View):

    def get(self, request):
        return render(request, 'app-add-schedules.html')

    def post(self, request):
        name = request.POST.get('name')
        description = request.POST.get('description')

        if Plan.objects.filter(name=name).exists():
            return render(request, 'app-add-schedules.html', {'error': 'Taki plan już istnieje'})

        if name == '' or description == '':
            return render(request, 'app-add-schedules.html', {'error1': 'Wypełnij wszytkie pola'})

        Plan.objects.create(name=name, description=description)

        return redirect('plans')


class AddRecipeToPlan(View):

    def get(self, request):
        recipes = Recipe.objects.all()
        plans = Plan.objects.all()
        days = NameOfTheDay.objects.all()

        ctx = {'recipes': recipes,
               'plans': plans,
               'days': days
               }

        return render(request, 'app-add-recipe-to-schedule.html', ctx)

    def post(self, request):
        plan_id = request.POST.get('plan')
        plan = Plan.objects.get(pk=plan_id)
        meal_name = request.POST.get('meal_name')
        order = request.POST.get('meal_number')
        recipe_id = request.POST.get('recipe')
        recipe = Recipe.objects.get(pk=recipe_id)
        day_id = request.POST.get('day')
        day = NameOfTheDay.objects.get(pk=day_id)

        RecipePlan.objects.create(meal_name=meal_name,
                                  order=order,
                                  recipe=recipe,
                                  plan=plan,
                                  day_name=day
                                  )

        return redirect(f'/plan/{plan_id}/')


class AboutView(View):

    def get(self, request):
        informations = Page.objects.all()
        information = Page.objects.all().count()

        for i in range(information):
            while informations[i].slug == 'about':
                ctx = {
                    'title': informations[i].title, 'description': informations[i].description
                }
                return render(request, 'about.html', ctx)
            return redirect("/#about")



