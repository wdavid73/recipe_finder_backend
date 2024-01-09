from rest_framework import serializers
from ..Model.ModelRecipe import Recipe

from recipe_finder_api.models import CustomUser
from recipe_finder_api.Category.Model.ModelCategory import Category
from recipe_finder_api.Ingredient.Model.ModelIngredient import Ingredient
from recipe_finder_api.Step.Model.ModelStep import Step, StepAction

from recipe_finder_api.AuthUser.Serializer.UserSerializer import UserSerializer
from recipe_finder_api.Ingredient.Serializer.SerializerIngredient import IngredientSerializer
from recipe_finder_api.Step.Serializer.SerializerStep import RecipeStepSerializer
from recipe_finder_api.Category.Serializer.SerializerCategory import CategorySerializer

class CreateRecipeSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Category.objects.filter(state=1),
        source='category'
    )
    
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=CustomUser.objects.all(),
        source='user'
    )
    

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'description',
            'cooking_time',
            'main_picture',
            'ratings',
            'preparation_video',
            'is_favorite',
            'category', 'category_id',
            'user','user_id',
        ]
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = set(self.context.get("fields", []))
        fields_to_exclude = set(self.context.get("not_fields", []))
        result = {}

        for field_name, field_value in representation.items():
            if (not fields_to_include or field_name in fields_to_include) and field_name not in fields_to_exclude:
                result[field_name] = field_value
        
        return result#
