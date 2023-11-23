from rest_framework import serializers
from ..Model.ModelOptionPictures import OptionPicturesRecipe
from recipe_finder_api.Recipe.Model.ModelRecipe import Recipe
from recipe_finder_api.Recipe.Serializer.SerializerRecipe import RecipeSerializer

class OptionPicturesRecipeSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = OptionPicturesRecipe
        fields = [
            'id',
            'picture',
            'recipe', 'recipe_id',
        ]
    

    def get_filtered_recipes(self, user):
        """
        Método para obtener las recetas filtradas por estado y usuario.
        """
        recipes = Recipe.objects.filter(state=2, user=user)
        return recipes

    def validate_recipe_id(self, value):
        """
        Valida y filtra la receta por estado y usuario.
        """
        user = self.context['request'].user
        filtered_recipes = self.get_filtered_recipes(user)
        
        try:
            # Intenta obtener la receta por el ID proporcionado
            recipe = filtered_recipes.get(pk=value)
            return recipe
        except Recipe.DoesNotExist:
            raise serializers.ValidationError("La receta seleccionada no es válida para el usuario actual.")

    def create(self, validated_data):
        # Extrae 'recipe_id' del diccionario de datos validados
        recipe_id = validated_data.pop('recipe_id')

        user = self.context.get('request').user
        filtered_recipes = self.get_filtered_recipes(user)

        try:
            # Obtiene la receta o crea una nueva si no existe
            recipe = filtered_recipes.get(pk=recipe_id)
        except Recipe.DoesNotExist:
            raise serializers.ValidationError("La receta seleccionada no es válida para el usuario actual.")

        # Asigna el ID de la receta al campo recipe_id
        validated_data['recipe_id'] = recipe_id

        # Crea la instancia de OptionPicturesRecipe sin guardarla todavía
        option_pictures_recipe = OptionPicturesRecipe(**validated_data)

        # Ahora puedes realizar cualquier validación adicional si es necesario

        # Guarda la instancia de OptionPicturesRecipe
        option_pictures_recipe.save()

        return option_pictures_recipe
