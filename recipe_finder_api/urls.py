from django.urls import path, include

urlpatterns = [
    path('auth/', include('recipe_finder_api.AuthUser.urls')),
    path('ingredient/', include('recipe_finder_api.Ingredient.urls')),
    path('category/', include('recipe_finder_api.Category.urls')),
    path('recipe/', include('recipe_finder_api.Recipe.urls'))
]