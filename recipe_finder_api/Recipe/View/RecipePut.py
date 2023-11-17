from django.shortcuts import get_object_or_404
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.viewsets import ModelViewSet
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelRecipe import Recipe
from ..Serializer.SerializerRecipe import RecipeSerializer


class UpdateRecipe(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenPermission]
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True)

        if serializer.is_valid():
            ingredient_ids = request.data.get('ingredients', [])
            instance.ingredient.set(ingredient_ids)
            serializer.save()
            return Response(
                {
                    'msg': 'Recipe Updated',
                    'data': serializer.data
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {'error': serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
