from rest_framework import permissions


class IsOwnUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print("Hello World")
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id
