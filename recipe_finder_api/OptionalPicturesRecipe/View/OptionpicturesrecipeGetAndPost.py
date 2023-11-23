from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from ..Model.ModelOptionPictures import OptionPicturesRecipe
from ..Serializer.SerializerOptionPictures import OptionPicturesRecipeSerializer

from recipe_finder.custom_permissions import TokenPermission


class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenPermission]

    def get(self, request: Request):
        optionpicturesrecipes = OptionPicturesRecipe.objects.filter(state=1)
        serializer = OptionPicturesRecipeSerializer(
            optionpicturesrecipes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(request_body=OptionPicturesRecipeSerializer)
    def post(self, request: Request):
        print(request.data)
        serializer = OptionPicturesRecipeSerializer(
            data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

