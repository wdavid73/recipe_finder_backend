from django.contrib.auth import logout
from rest_framework import status, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token


class LogoutAPI(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request) -> Response:
        try:
            token = Token.objects.get(key=request.data["token"])
            token.delete()
            logout(request)
            return Response({'data': 'You are logout'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist as e:
            return Response({'error': 'Token doesn´t exist.'}, status=status.HTTP_404_NOT_FOUND)
