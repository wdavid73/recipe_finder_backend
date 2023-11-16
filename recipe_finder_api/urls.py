from django.urls import path, include

urlpatterns = [
    path('auth/', include('recipe_finder_api.AuthUser.urls')),
    path('ingredient/', include('recipe_finder_api.Ingredient.urls')),
]