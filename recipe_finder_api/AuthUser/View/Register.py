from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import generics
from ..Serializer.UserSerializer import UserSerializer
from ..Serializer.RegisterSerializer import RegisterSerializer
from ..Serializer.TokenSerializer import TokenSerializer


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        new_data = request.data.copy()
        new_data['username'] = new_data["email"].split("@")[0]
        serializer = self.get_serializer(data=new_data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = Token.objects.create(user=user)
        serializer_token = TokenSerializer(token, context={'request': request})
        return Response(
            {
                "user": UserSerializer(user, context={'request': request}).data,
                "token": serializer_token.data
            },
            status=status.HTTP_201_CREATED,
        )
