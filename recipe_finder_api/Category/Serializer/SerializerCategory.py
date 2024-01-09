from rest_framework import serializers
from ..Model.ModelCategory import Category

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']
