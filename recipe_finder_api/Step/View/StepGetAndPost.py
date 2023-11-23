from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelStep import Step
from ..Serializer.SerializerStep import StepSerializer

class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated, TokenPermission]
    def get(self, request: Request):
        steps = Step.objects.filter(state=1)
        serializer = StepSerializer(
            steps, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(
        request_body=StepSerializer,
        responses={
            201: "Creado exitosamente",
            400: "Solicitud incorrecta: verifica la estructura de los datos",
            403: "Permiso denegado: el usuario no tiene permisos suficientes",
            500: "Error interno del servidor"
        },
        operation_summary="Crear un nuevo step",
        operation_description="Este endpoint permite la creación de un nuevo step.",
    )
    def post(self, request: Request):
        serializer = StepSerializer(
            data=request.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

