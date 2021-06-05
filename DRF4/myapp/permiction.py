from rest_framework.permissions import BasePermission,SAFE_METHODS
class Read_only(BasePermission):
    def has_permission(self,request,view):
        if request.method is SAFE_METHODS:
            return True
        else:
            return False