from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from user.models import User


class UserMixin(serializers.Serializer):
    email = serializers.EmailField(validators=[
        UniqueValidator(queryset=User.objects.all())
    ])
    password = serializers.CharField(max_length=128, write_only=True)

    def validate_password(self, value: str) -> str:
        password_validation.validate_password(value, self.instance)
        hashed_password = make_password(value)
        return hashed_password
