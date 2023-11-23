from django.urls import path
from .View.RecipeGetAndPost import GetAndPost
from .View.RecipePut import UpdateRecipe
from .View.RecipeDelete import disable_recipe, delete_recipe
from .View.RecipeByUser import GetRecipeByUser
from .View.RecipeDetails import details_recipe

urlpatterns = [
    path("", GetAndPost.as_view(), name="get_and_post"),
    path("update/<int:pk>", UpdateRecipe.as_view({'put': 'update'}), name="update_recipe"),
    path("disable/<int:id>", disable_recipe, name="disable_recipe"),
    path("delete/<int:id>", delete_recipe, name="delete_recipe"),
    path("by_user/", GetRecipeByUser.as_view(), name="get_by_user"),
    path('details/<int:id>', details_recipe, name="details_recipe")
]
