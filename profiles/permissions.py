from rest_framework import permissions


class HasProfileOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.has_profile or
            request.method in permissions.SAFE_METHODS
        )
