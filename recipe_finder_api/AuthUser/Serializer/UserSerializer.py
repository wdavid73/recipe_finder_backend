from typing import Any
from django.contrib.auth.base_user import AbstractBaseUser
from django.http.request import HttpRequest
from rest_framework import serializers
from django.contrib.auth import authenticate
from recipe_finder_api.models import CustomUser

from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class EmailBackend(ModelBackend):
    def authenticate(self, request: HttpRequest, username=None, password=None, **kwargs: Any) -> AbstractBaseUser:
        CustomUser = get_user_model()
        try:
            user = CustomUser.objects.get(email=username)
        except CustomUser.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'name', 'profile_picture', 'birthday')

    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if username and password:
            user = authenticate(request=self.context.get(
                'request'), username=username, password=password,)
            if not user:
                msg = 'Unable to login with username and password.'
                raise serializers.ValidationError(msg, code='authorization')

        elif email and password:
            user = authenticate(request=self.context.get(
                'request'), email=email, password=password,)
            if not user:
                msg = 'Unable to login with email and password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" or "email" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        data['user'] = user
        return data



