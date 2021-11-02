from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import DEFAULT_DB_ALIAS, router
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from . import fields


class User(AbstractUser):
    @property
    def token(self):
        try:
            return self.auth_token.key
        except Token.DoesNotExist:
            return None

    @property
    def permissions(self):  # statistics ex
        permissions = None
        if self.is_superuser:
            permissions = Permission.objects.all()
        else:
            permissions = self.user_permissions.all() | Permission.objects.filter(group__user=self)
        return sorted([permission.codename for permission in permissions])


class BaseUploadedFile(models.Model):
    file = None
    object = None

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created = fields.CreatedField()

    class Meta:
        abstract = True
