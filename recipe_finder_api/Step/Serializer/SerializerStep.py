from rest_framework import serializers
from ..Model.ModelStep import Step, StepAction
from recipe_finder_api.Recipe.Model.ModelRecipe import Recipe
from recipe_finder_api.Recipe.Serializer.SerializerRecipe import RecipeSerializer


class StepSerializer(serializers.ModelSerializer):
    recipe = RecipeSerializer(read_only=True, context={'not_fields': ['user']})
    recipe_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Recipe.objects.all(),
        source='recipe'
    )


    class Meta:
        model = Step
        fields = ['id', 'name', 'recipe', 'recipe_id']

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = set(self.context.get("fields", []))
        fields_to_exclude = set(self.context.get("not_fields", []))
        result = {}

        for field_name, field_value in representation.items():
            if (not fields_to_include or field_name in fields_to_include) and field_name not in fields_to_exclude:
                result[field_name] = field_value
        
        return result



class StepActionSerializer(serializers.ModelSerializer):
    step = StepSerializer(read_only=True)
    step_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Step.objects.all(),
        source="step"
    )

    class Meta:
        model = StepAction
        fields = ['id', 'action', 'step', 'step_id']

    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        fields_to_include = set(self.context.get("fields", []))
        fields_to_exclude = set(self.context.get("not_fields", []))
        result = {}

        for field_name, field_value in representation.items():
            if (not fields_to_include or field_name in fields_to_include) and field_name not in fields_to_exclude:
                result[field_name] = field_value
        
        return result

class CreateRecipeStepActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StepAction
        fields = ['action']
        
class RecipeStepSerializer(serializers.ModelSerializer):
    actions = CreateRecipeStepActionSerializer(many=True)

    class Meta:
        model = Step
        fields = ['name', 'actions']
        