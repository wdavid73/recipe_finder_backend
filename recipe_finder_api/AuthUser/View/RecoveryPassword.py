from django.contrib.auth.hashers import make_password, MD5PasswordHasher
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from recipe_finder_api.models import CustomUser
from recipe_finder_api.AuthUser.Serializer.RecoveryPasswordSerializer import RecoveryPasswordSerializer


class RecoveryPasswordAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request) -> Response:
        serializer = RecoveryPasswordSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        if (serializer.data['new_password'] == serializer.data['confirm_new_password']):
            user = CustomUser.objects.get(email=serializer.data['email'])
            user.password = make_password(serializer.data['new_password'])
            user.save()
            return Response({"data": "Password updated"}, status=status.HTTP_200_OK)
        return Response({"error": "Password don´t match, Please try again"}, status=status.HTTP_400_BAD_REQUEST)
