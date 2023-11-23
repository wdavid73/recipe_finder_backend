import django_filters
from ..Model.ModelRecipe import Recipe

class RecipeFilters(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    cooking_time = django_filters.NumberFilter()
    ratings = django_filters.NumberFilter()
    category = django_filters.CharFilter(field_name='category__name', lookup_expr='icontains')
    is_favorite = django_filters.BooleanFilter()

    class Meta:
        model = Recipe
        fields = ['name', 'cooking_time', 'ratings', 'is_favorite', 'category']