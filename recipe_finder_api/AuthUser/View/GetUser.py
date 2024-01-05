from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from ..Serializer.UserSerializer import UserSerializer

class GetUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request) -> Response:
        serializer = UserSerializer(request.user, context={'request': request})
        return Response(serializer.data,status=status.HTTP_200_OK)
