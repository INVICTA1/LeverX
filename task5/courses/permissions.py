from rest_framework import permissions


class IsTeacherOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS
                    or request.user.pk and request.user.profile == 'teacher')


class IsStudentOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS
                    or request.user.pk and request.user.profile == 'student')