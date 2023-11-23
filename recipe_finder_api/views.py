from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.authentication import TokenAuthentication
from recipe_finder.custom_permissions import TokenPermission

class TuVista(APIView):
    permission_classes = [IsAuthenticated, TokenPermission]
    # authentication_classes = [TokenAuthentication]

    def get(self, request):
        # Tu lógica de vista aquí
        return Response({"mensaje": "Hola, mundo!"})