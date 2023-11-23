from django.db.models import Count
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from ..Model.ModelRecipe import Recipe
from ..Serializer.SerializerRecipe import RecipeSerializer, SerializerRecipeIngredient
from ..utils.RecipeFilter import RecipeFilters

from recipe_finder.custom_permissions import TokenPermission


class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilters
    

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('skip', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=0),
        openapi.Parameter('limit', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER, default=10),
        openapi.Parameter('name', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
        openapi.Parameter('cooking_time', in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER),
        openapi.Parameter('ratings', in_=openapi.IN_QUERY, type=openapi.TYPE_NUMBER),
        openapi.Parameter('is_favorite', in_=openapi.IN_QUERY, type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('category', in_=openapi.IN_QUERY, type=openapi.TYPE_STRING),
    ])

    def get(self, request: Request):
        queryset = Recipe.objects.filter(state=2)
        if request.query_params:
            filter_instance = self.filterset_class(request.query_params, queryset=queryset)
            queryset = filter_instance.qs
        
        skip = int(request.query_params.get('skip', 0))
        limit = int(request.query_params.get('limit', 10))

        total_count = queryset.aggregate(total_count=Count('id'))['total_count']
        paginated_queryset = queryset[skip:skip + limit]
        serializer = RecipeSerializer(paginated_queryset, many=True, context={'not_fields': ['user']})

        return Response({
            'total': total_count,
            'skip': skip,
            'limit': limit,
            'data': serializer.data,
        }, status=status.HTTP_200_OK)

    def post(self, request: Request):
        try:
            new_recipe = request.data.copy()
            ingredients_selected = new_recipe["ingredients"]

            del new_recipe["ingredients"]

            serializer_recipe = RecipeSerializer(
                data=new_recipe, context={'request': request})

            if serializer_recipe.is_valid():
                serializer_recipe.save()

                serializer_ingredient = save_recipe_ingredient(
                    serializer_recipe.data["id"], ingredients_selected, request
                )

                return Response(
                    {
                        "recipe": serializer_recipe.data,
                        "ingredients": serializer_ingredient
                    },
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(serializer_recipe.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise ParseError(f"an error occurred with {e}")


def save_recipe_ingredient(idRecipe: int, ingredients, request: Request):
    items = []
    for ingredient in ingredients:
        data = {}
        data["ingredient_id"] = ingredient
        data["recipe_id"] = idRecipe
        serializer = SerializerRecipeIngredient(
            data=data, context={'request': request, 'fields' : ['ingredient']}
        )
        if serializer.is_valid():
            serializer.save()
            items.append(serializer.data)
        else:
            return serializer.errors
    return items
