from rest_framework.permissions import BasePermission

class IsSuperAdminUser(BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return bool(user.is_authenticated and user.is_superuser)
        

