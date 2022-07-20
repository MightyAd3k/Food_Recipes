from django.urls import path
from food import views

urlpatterns = [
    path('main/', views.Dashboard.as_view(), name='main_page'),

    path('recipe/list/', views.RecipeList.as_view(), name='recipes'),
    path('recipe/add/', views.AddRecipe.as_view(), name='add_recipe'),
    path('recipe/<int:pk>/', views.RecipeDetails.as_view(), name='recipe_details'),
    path('recipe/modify/<int:pk>/', views.UpdateRecipe.as_view(), name='update_recipe'),
    path('recipe/delete/<int:pk>/', views.DeleteRecipe.as_view(), name='delete_recipe'),

    path('plan/list/', views.PlanList.as_view(), name='plans'),
    path('plan/<int:pk>/', views.PlanDetails.as_view(), name='plan_details'),
    path('plan/add/', views.AddPlan.as_view(), name='add_plan'),
    path('plan/add-recipe/', views.AddRecipeToPlan.as_view(), name='add_recipe_to_plan'),
    path('plan/modify/<int:pk>/', views.UpdatePlan.as_view(), name='update_plan'),
    path('plan/delete/<int:pk>/', views.DeletePlan.as_view(), name='delete_plan'),
    path('delete_recipe_from_plan/<int:plan_pk>/<int:recipe_pk>/', views.DeleteRecipeFromPlan.as_view(), name='delete_recipe_from_plan'),

    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact')
]
