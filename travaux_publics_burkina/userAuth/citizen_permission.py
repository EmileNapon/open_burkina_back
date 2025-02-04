from rest_framework import permissions

class IsCitoyen(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'citoyen'
     
class CanModify(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role=='citoyen'