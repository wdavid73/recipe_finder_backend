from rest_framework import permissions
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import PermissionDenied


class TokenPermission(permissions.BasePermission):

    """Token Permission verifed if token supplied exists

    Returns:
        [Boolean]: [True if token exists , False if not]
    """

    message = "Authentication Token Invalid"

    def has_permission(self, request, view):
        headers = request.headers
        authorization_keys = ['authorization', 'Authorization']
        for key in authorization_keys:
            if key in headers:
                AuthToken = headers[key].split(" ")[1]
                try:
                    Token.objects.get(key=AuthToken)
                    return True
                except Token.DoesNotExist:
                    raise PermissionDenied(
                        "Your supplied token does not exist", 401)
            else:
                raise PermissionDenied(
                    "You dont send Authorization in headers", 401)
