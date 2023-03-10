from typing import Callable
from collections import OrderedDict

from rest_framework.request import Request
from rest_framework.serializers import Serializer
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject
from rest_framework.permissions import IsAdminUser

from app.models import Company, Candidate
from user.serializer_mixins import UserMixin
from user.models import User


def to_representation_with_user(
    self: Serializer, instance: Candidate | Company, user: User
):
    '''
    A custom to_representation since we need to serialize data from two models: 
    Candidate or Company, User
    '''
    ret = OrderedDict()
    fields = self._readable_fields

    user_serializer_fields_name: list[str] = list(
        f.field_name for f in UserMixin(instance=user)._readable_fields
    )
    for field in fields:
        try:
            # Check if current field in UserMixin serializator, 
            # if field not in instance or user then AttributeError
            if field.field_name in user_serializer_fields_name:
                attribute = field.get_attribute(user)
            else:
                attribute = field.get_attribute(instance)
        except SkipField:
            continue

        check_for_none = attribute.pk \
            if isinstance(attribute, PKOnlyObject) else attribute
        if check_for_none is None:
            ret[field.field_name] = None
        else:
            ret[field.field_name] = field.to_representation(attribute)

    return ret


def is_admin_or_superuser(func: Callable):
    '''
    Decorator for `has_permission` method that returns True if the user is
    an `admin` or `superuser`.\n 
    Otherwise result of `has_permission` execution.
    '''
    def wrapper(self, request: Request, view) -> bool:
        if request.user and request.user.is_authenticated \
                and (request.user.is_staff or request.user.is_superuser):
            return True
        return func(self, request, view)
    return wrapper
