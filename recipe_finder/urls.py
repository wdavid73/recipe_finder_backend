from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .authentication import CustomAuthentication

schema_view = get_schema_view(
    openapi.Info(
        title="Recipe Finder API",
        default_version='v1',
        description="Descripción de tu API",
        terms_of_service="https://www.guichodevs.com/terms/",
        contact=openapi.Contact(email="guichodevs@gmail.com.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[CustomAuthentication]
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipe_finder_api.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]
