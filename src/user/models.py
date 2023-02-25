from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.hashers import make_password

from app.models import Company, Candidate


class UserManager(BaseUserManager):
    # use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('User must have email')
        user: User = self.model(
            email=self.normalize_email(email),
            **extra_fields
        )
        user.password = make_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        if 'is_staff' not in extra_fields:
            extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser):
    objects = UserManager()

    email = models.EmailField(verbose_name='email', unique=True)
    password = models.CharField(verbose_name='password', max_length=128)
    company = models.OneToOneField(
        to=Company,
        verbose_name='company',
        on_delete=models.CASCADE,
        related_name='owner',
        null=True, blank=True
    )
    candidate = models.OneToOneField(
        to=Candidate,
        verbose_name='candidate',
        on_delete=models.CASCADE,
        related_name='user',
        null=True, blank=True
    )

    is_superuser = models.BooleanField(verbose_name='superuser', default=False)
    is_staff = models.BooleanField(verbose_name='staff', default=False)
    is_active = models.BooleanField(verbose_name='active', default=True)

    USERNAME_FIELD = 'email'
    

class Staff(models.Model):
    company = models.ForeignKey(
        to=Company, 
        verbose_name='company', 
        on_delete=models.CASCADE, 
        related_name='staff'
    )
    employee = models.ForeignKey(
        to=User, 
        verbose_name='employee', 
        on_delete=models.CASCADE, 
        related_name='workplace'
    )
    permissions = models.CharField(
        verbose_name='permissions', max_length=128, null=True, blank=True
    )
