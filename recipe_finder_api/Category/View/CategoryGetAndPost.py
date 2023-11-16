from rest_framework import status, permissions
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from recipe_finder.custom_permissions import TokenPermission

from ..Model.ModelCategory import Category
from ..Serializer.SerializerCategory import CategorySerializer


class GetAndPost(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request):
        categorys = Category.objects.filter(state=1)
        serializer = CategorySerializer(
            categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request: Request):
        serializer = CategorySerializer(
            data=request.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated, TokenPermission])
def create_multiple_category(request: Request):
    categories_data = request.data.get("categories", [])
    existing_name = set(
        Category.objects.values_list("name", flat=True).distinct()
    )

    validated_data = [
        category for category in categories_data
        if (name := category.get("name", "").lower()) not in existing_name and existing_name.add(name) is None
    ]

    serialized = CategorySerializer(data=validated_data, many=True)
    if serialized.is_valid():
        serialized.save()
        return Response(
            {"data": serialized.data},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {'error': serialized.errors},
            status=status.HTTP_400_BAD_REQUEST
        )
