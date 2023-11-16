from django.urls import path
from .View.IngredientGetAndPost import GetAndPost, create_multiple_ingredient

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path('create_multiple/', create_multiple_ingredient, name="create_multiple_ingredients")
]
