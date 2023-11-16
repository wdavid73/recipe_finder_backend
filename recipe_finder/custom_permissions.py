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
        if 'Authorization' in request.headers:
            AuthToken = request.META['HTTP_AUTHORIZATION'].split(" ")[1]
            try:
                Token.objects.get(key=AuthToken)
                return True
            except Token.DoesNotExist:
                raise PermissionDenied(
                    "You dont have permission to this action", 401)
        else:
            raise PermissionDenied(
                "You dont send Authorization in headers", 401)
