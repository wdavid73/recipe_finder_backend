from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelRecipe import Recipe
from ..Serializer.SerializerRecipe import RecipeSerializer


@api_view(['GET'])
@permission_classes([TokenPermission, IsAuthenticated])
def details_recipe(request: Request, id: int) -> Response:
    try:
        recipe = Recipe.objects.prefetch_related(
            'ingredient').get(id=id, user=request.user)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RecipeSerializer(recipe)

    return Response(
        {
            'recipe': serializer.data,
            'ingredients': serializer.get_ingredients(recipe)
        },
        status=status.HTTP_200_OK
    )
