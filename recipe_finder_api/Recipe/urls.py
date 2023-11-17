from django.urls import path
from .View.RecipeGetAndPost import GetAndPost
from .View.RecipePut import UpdateRecipe
from .View.RecipeDelete import disable_recipe, delete_recipe

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("update/<int:pk>", UpdateRecipe.as_view({'put': 'update'}), name="update_recipe"),
    path("disable/<int:id>", disable_recipe, name="disable_recipe"),
    path("delete/<int:id>", delete_recipe, name="delete_recipe")
]
