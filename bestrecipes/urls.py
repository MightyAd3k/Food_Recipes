"""bestrecipes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from food.views import LandingPage, RecipeList, Dashboard, AddRecipe, PlanList, PlanDetails, \
    UpdateRecipe, RecipeDetails, DeleteRecipe, AddPlan

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LandingPage.as_view()),
    path('main/', Dashboard.as_view(), name='main_page'),

    path('recipe/list/', RecipeList.as_view(), name='recipes'),
    path('recipe/add/', AddRecipe.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/', RecipeDetails.as_view(), name='recipe_details'),
    path('recipe/modify/<int:pk>/', UpdateRecipe.as_view(), name='update_recipe'),
    path('recipe/delete/<int:pk>/', DeleteRecipe.as_view(), name='delete_recipe'),

    path('plan/list/', PlanList.as_view(), name='plans'),
    path('plan/<int:pk>/', PlanDetails.as_view(), name='plan_details'),
    path('plan/add/', AddPlan.as_view(), name='add_plan'),
    #path('path/add-recipe/', AddRecipeToPlan.as_view(), name='add_recipe_to_plan'),
]
