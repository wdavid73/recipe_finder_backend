from rest_framework import serializers
from ..Model.ModelRecipe import ExtraImage

class ExtraImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = ExtraImage
    fields = ['id', 'picture']