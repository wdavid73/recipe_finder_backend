from django.urls import path
from .View.StepGetAndPost import GetAndPost
from .View.StepActionGetAndPost import ActionGetAndPost

urlpatterns = [
    path("" , GetAndPost.as_view() , name="get_and_post"),
    path("action/" , ActionGetAndPost.as_view() , name="get_and_post"),
]
