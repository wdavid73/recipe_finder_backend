from django.urls import path
from .View.Register import RegisterAPI
from .View.Login import LoginAPI
from .View.Logout import LogoutAPI
from .View.RecoveryPassword import RecoveryPasswordAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('recovery_password/', RecoveryPasswordAPI.as_view(), name='recovery_password'),
]
