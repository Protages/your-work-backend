from rest_framework import status, viewsets


class PermissionMixin:
    '''
    Mixin to provide a method `get_permissions`.\n
    Need to define in ViewSet `permission_class_by_action`
    in format `{'create': [IsAuthenticated]}`.
    '''
    permission_classes_by_action: dict[str, list] = {}

    def get_permissions(self):
        try:
            # return permission_classes depending on `action` 
            return [permission() for permission in \
                    self.permission_classes_by_action[self.action]]
        except KeyError: 
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]
