from django.urls import path, include

urlpatterns = [
    path('auth/', include('recipe_finder_api.AuthUser.urls')),
]