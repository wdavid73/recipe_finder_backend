from django.urls import path
from .View.CategoryGetAndPost import GetAndPost, create_multiple_category

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path("create_multiple/", create_multiple_category, name="create_multiple_categories"),
]
