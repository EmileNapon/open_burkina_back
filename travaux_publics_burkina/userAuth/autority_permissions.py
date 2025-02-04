from rest_framework import permissions

class IsAutorite(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'autorite'  

class CanUpdateProject(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'autorite'  
    
class CanViewReports(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'autorite'  