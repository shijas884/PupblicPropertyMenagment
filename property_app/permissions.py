from rest_framework.permissions import BasePermission


# permissions class

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role_type == 'ADMIN'
    

class IsWriterOrAdnin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role_type in  ['ADMIN','WRITER']
    

class IsViewer(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role_type in ['ADMIN','WRITER','VIEWER']

