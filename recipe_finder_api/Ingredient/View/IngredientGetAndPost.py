from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from recipe_finder.custom_permissions import TokenPermission
from ..Model.ModelIngredient import Ingredient
from ..Serializer.SerializerIngredient import IngredientSerializer


class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request):
        ingredients = Ingredient.objects.filter(state=1)
        serializer = IngredientSerializer(
            ingredients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = IngredientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated, TokenPermission])
def create_multiple_ingredient(request: Request):
    ingredients_data = request.data.get("ingredients", [])
    existing_name = set(
        Ingredient.objects.values_list("name", flat=True).distinct()
    )

    validated_data = [
        ingredient_data for ingredient_data in ingredients_data
        if (name := ingredient_data.get("name", "").lower()) not in existing_name and existing_name.add(name) is None
    ]

    serialized = IngredientSerializer(data=validated_data, many=True)
    if serialized.is_valid():
        serialized.save()
        return Response(
            {"data": serialized.data},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'error': serialized.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
