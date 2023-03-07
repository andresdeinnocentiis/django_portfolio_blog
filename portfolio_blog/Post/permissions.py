from rest_framework import permissions

"""
I created this in order to establish permissions to delete/update since I need unregistered users to also be able to execute those actions
and I can't ask for authorization nor for authentication for them.
And if I didn't set any permission, then anyone would be able to delete or update everybody's review or comment.
"""

class CanDelete(permissions.BasePermission):
    """
    Custom permission to allow unauthenticated users to delete their own reviews or comments,
    but require authentication to delete reviews or comments belonging to other users.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the request method is DELETE
        if request.method == 'DELETE':
            # Check if the user is the owner
            if request.data['userInfo']:
                user_info = request.data['userInfo']
                if user_info.get('anonymous_identifier') and str(obj.anonymous_user.anonymous_identifier) == user_info.get('anonymous_identifier'):
                    # I parsed to string "obj.anonymous_user.anonymous_identifier" because it's a uuid obj.
                    return True                    
                elif ((obj.user and obj.user.id) and user_info.get('id') == obj.user.id) or user_info.get('isAdmin'):
                    return True

            else:
                return False
        else:
            # Allow read-only access to the view
            return True


class CanUpdate(permissions.BasePermission):
    """
    Custom permission to allow unauthenticated users to update their own reviews or comments,
    but require authentication to update reviews or comments belonging to other users.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the request method is PUT
        if request.method == 'PUT':
            # Check if the user is the owner      
     
            if request.data.get('userInfo'):

                user_info = request.data['userInfo']
                if user_info.get('anonymous_identifier') and str(obj.anonymous_user.anonymous_identifier) == user_info.get('anonymous_identifier'):
                    # I parsed to string "obj.anonymous_user.anonymous_identifier" because it's a uuid obj.
                    return True                    
                elif ((obj.user and obj.user.id) and user_info.get('id') == obj.user.id):

                    return True

            else:
                return False
        else:
            # Allow read-only access to the view
            return True
