from rest_framework import permissions
    
class IsCitoyen(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'citoyen' 
    
class IsAutority(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'autority' 
    
class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'supplier' 
    
class CanViewCitoyens(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class CanDeleteCitoyen(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class CanModifyVerification(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class CanBlockCitoyen(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

class CanChangeRole(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser

