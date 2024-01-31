from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only owners of an object to edit it.
    Read-only permissions are allowed for any user.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the requesting user has permission to perform the requested action on the object.
        """
        # Allow read-only access for safe methods (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
