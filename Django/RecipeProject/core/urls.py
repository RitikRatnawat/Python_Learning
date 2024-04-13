from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.recipes, name="recipe_add"),
    path('delete/<int:recipe_id>', views.recipe_delete, name="recipe_delete"),
    path('update/<int:recipe_id>', views.recipe_update, name="recipe_update"),
]