from rest_framework import serializers
from django.contrib.auth.models import User

from recipe_finder_api.models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('id', 'username', 'name', 'email', 'birthday', 'password')
    extra_kwargs = { 'password': { 'write_only': True } }

  def create(self, validated_data):
    user = CustomUser.objects.create_user(
      validated_data['username'],
      validated_data['email'],
      validated_data['password'],
      validated_data['birthday'],
      validated_data['name'],
    )
    return user