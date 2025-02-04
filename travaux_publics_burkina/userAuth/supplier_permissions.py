from rest_framework import permissions

class IsPrestataire(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'prestataire'  
    
class CanJustifyDelaysAndNonConformities(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'prestataire' and view.action in ['create', 'update', 'partial_update']

class CanViewCitizenReports(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'prestataire'

class CanViewOwnProjects(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'prestataire' and view.get_object().is_assigned_to(request.user)
