from django.contrib.auth import login
from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from ..Serializer.UserSerializer import UserSerializer


class LoginAPI(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthTokenSerializer

    def post(self, request: Request) -> Response:
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                'user': UserSerializer(user, context={'request': request}).data,
                'token': token.key,
                'token_created': created,
            },
            status=status.HTTP_200_OK,
        )
