from rest_framework import serializers
from recipe_finder_api.models import CustomUser

class RecoveryPasswordSerializer(serializers.Serializer):
   email= serializers.EmailField()
   new_password = serializers.CharField()
   confirm_new_password = serializers.CharField()
   class Meta:
         model = CustomUser
         fields  = ('email', "new_password" ,"confirm_new_password")
