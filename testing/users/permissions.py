from rest_framework.permissions import BasePermission,SAFE_METHODS

class TeacherOnly(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and hasattr(request.user, "teacher")
            and request.user.member.is_active
            and request.user.member.is_manager
        )

class StudentOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and hasattr(request.user, "student")

class IsOwnerProfileOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user==request.user