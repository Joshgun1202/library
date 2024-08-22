from rest_framework import permissions


class AllowAnySignUp(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create' or view.action == 'regenerate_otp' or view.action == 'verify_otp':
            return True
        else:
            return request.user and request.user.is_authenticated