from rest_framework import permissions
from rest_framework.authentication import SessionAuthentication


class IsGetOrIsAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        # allow all POST requests
        if request.method == 'GET':
            return True

        # Otherwise, only allow authenticated requests
        # Post Django 1.10, 'is_authenticated' is a read-only attribute
        return request.user and request.user.is_authenticated


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return
