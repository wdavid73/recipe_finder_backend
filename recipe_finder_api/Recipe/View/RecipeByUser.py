from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelRecipe import Recipe
from ..Serializer.SerializerRecipe import RecipeSerializer
from ..utils.RecipeFilter import RecipeFilters
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class GetRecipeByUser(APIView):
    permission_classes = [IsAuthenticated, TokenPermission]
    filter_backends = [DjangoFilterBackend]
    filterset_class = RecipeFilters

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('skip', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER, default=0),
        openapi.Parameter('limit', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER, default=10),
        openapi.Parameter('name', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_STRING),
        openapi.Parameter('cooking_time', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_INTEGER),
        openapi.Parameter('ratings', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('is_favorite', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_BOOLEAN),
        openapi.Parameter('category', in_=openapi.IN_QUERY,
                          type=openapi.TYPE_STRING),
    ])
    def get(self, request: Request) -> Response:
        recipes = Recipe.objects.filter(state=2, user=request.user)

        if request.query_params:
            filter_instance = RecipeFilters(
                request.query_params, queryset=recipes)
            recipes = filter_instance.qs

        skip = int(request.query_params.get('skip', 0))
        limit = int(request.query_params.get('limit', 10))

        total_count = recipes.count()

        paginated_recipes = recipes[skip:skip + limit]

        serializer = RecipeSerializer(paginated_recipes, many=True, context={
                                      'not_fields': ['user']})

        return Response(
            {
                'total': total_count,
                'skip': skip,
                'limit': limit,
                'data': serializer.data
            },
            status=status.HTTP_200_OK
        )
