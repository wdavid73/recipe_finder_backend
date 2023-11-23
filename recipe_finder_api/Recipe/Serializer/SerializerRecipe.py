from rest_framework import serializers
from ..Model.ModelRecipe import Recipe, Recipe_Ingredient
from .ExtraImageSerializer import ExtraImageSerializer

from recipe_finder_api.models import CustomUser
from recipe_finder_api.Category.Model.ModelCategory import Category
from recipe_finder_api.Ingredient.Model.ModelIngredient import Ingredient
from recipe_finder_api.Step.Model.ModelStep import Step, StepAction

from recipe_finder_api.AuthUser.Serializer.UserSerializer import UserSerializer
from recipe_finder_api.Category.Serializer.SerializerCategory import CategorySerializer
from recipe_finder_api.Ingredient.Serializer.SerializerIngredient import IngredientSerializer

class ReadStepActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepAction
        fields = ['action']

class ReadStepSerializer(serializers.ModelSerializer):
    actions = ReadStepActionSerializer(many=True, read_only=True, source='stepaction_set')

    class Meta:
        model = Step
        fields = ['name', 'actions']


class RecipeSerializer(serializers.ModelSerializer):

    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Category.objects.filter(state=1),
        source='category'
    )

    user = UserSerializer(read_only=True)

    ingredients = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Ingredient.objects.all(),
        many=True,
        required=False
    )

    extra_images = ExtraImageSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'name',
            'description',
            'cooking_time',
            'is_favorite',
            'main_picture',
            'category', 'category_id',
            'user',
            'ingredients',
            'extra_images',
        ]
        

    def get_ingredients(self, obj):
        ingredients = obj.ingredient.all()
        return IngredientSerializer(ingredients, many=True).data
    
    def get_steps(self, obj):
        steps = Step.objects.filter(recipe=obj)
        return ReadStepSerializer(steps, many=True).data
    
    def update(self, instance, validated_data):
        ingredients_data = validated_data.pop('ingredients', [])
        instance = super(RecipeSerializer, self).update(instance, validated_data)
        instance.ingredient.set(ingredients_data)
        return instance
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = set(self.context.get("fields", []))
        fields_to_exclude = set(self.context.get("not_fields", []))
        result = {}

        for field_name, field_value in representation.items():
            if (not fields_to_include or field_name in fields_to_include) and field_name not in fields_to_exclude:
                result[field_name] = field_value
        
        return result


class SerializerRecipeIngredient(serializers.ModelSerializer):
    ingredient = IngredientSerializer(read_only=True)
    ingredient_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Ingredient.objects.filter(state=1),
        source='ingredient'
    )

    recipe = RecipeSerializer(read_only=True)
    recipe_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Recipe.objects.all(),
        source='recipe'
    )

    class Meta:
        model = Recipe_Ingredient
        fields = [
            'id',
            'ingredient', 'ingredient_id',
            'recipe', 'recipe_id',
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = set(self.context.get("fields", []))
        result = {}

        for field_name, field_value in representation.items():
            if not fields_to_include or field_name in fields_to_include:
                result[field_name] = field_value
        
        return result
