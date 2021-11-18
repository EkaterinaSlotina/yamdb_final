from rest_framework import permissions


class IsAdminUserOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS or (
            request.user.is_authenticated) and (
            request.user.is_staff or request.user.is_admin)


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and (
            request.user.is_staff or request.user.is_admin
        )


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.author == request.user


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or (
            request.user.is_moderator))


class ReviewPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (obj.author == request.user or request.method in
                permissions.SAFE_METHODS or request.user.is_moderator
                or request.user.is_admin)
