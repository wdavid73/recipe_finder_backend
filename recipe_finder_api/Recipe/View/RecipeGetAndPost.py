from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework.views import APIView

from ..Model.ModelRecipe import Recipe
from ..Serializer.SerializerRecipe import RecipeSerializer, SerializerRecipeIngredient


from recipe_finder.custom_permissions import TokenPermission


class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenPermission]

    def get(self, request: Request):
        recipes = Recipe.objects.filter(state=1)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

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
