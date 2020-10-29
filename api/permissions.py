from rest_framework import permissions


class IsAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'admin'


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'moderator'


class IsAdminOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return ((request.method in permissions.SAFE_METHODS) or (request.user.role == 'admin'))
