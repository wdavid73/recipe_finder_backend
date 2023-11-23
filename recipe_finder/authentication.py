from rest_framework.authentication import BasicAuthentication
from rest_framework.exceptions import AuthenticationFailed
from recipe_finder_api.models import CustomUser


class CustomAuthentication(BasicAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("authorization")

        if not auth_header:
            return None

        try:
            token = auth_header.split(' ')[1]
            user = CustomUser.objects.get(auth_token__key=token)
        except CustomUser.DoesNotExist:
            raise AuthenticationFailed(
                'No se encontró un usuario con este token {}'.format(token),
            )
        except IndexError:
            raise AuthenticationFailed('No se proporcionó un token válido')
        return (user, None)

    def authenticate_header(self, request):
        return 'Token'
