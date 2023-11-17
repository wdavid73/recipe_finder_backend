from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelRecipe import Recipe

@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated, TokenPermission])
def disable_recipe(request: Request, id: int) -> Response:
  recipe = get_object_or_404(Recipe, id=id)
  recipe.state = 0
  recipe.save()
  return Response({ 'msg': 'Recipe disabled'}, status=status.HTTP_204_NO_CONTENT)


@api_view(["DELETE"])
@permission_classes([permissions.IsAuthenticated, TokenPermission])
def delete_recipe(request: Request, id: int) -> Response:
  recipe = get_object_or_404(Recipe, id=id)
  recipe.delete()
  return Response({'msg': 'Recipe delete'}, status=status.HTTP_204_NO_CONTENT)
