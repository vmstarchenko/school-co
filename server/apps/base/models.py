from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import DEFAULT_DB_ALIAS, router
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    @property
    def token(self):
        # pylint: disable=no-member
        return self.auth_token.key

    @property
    def permissions(self):
        permissions = None
        if self.is_superuser:
            permissions = Permission.objects.all()
        else:
            permissions = self.user_permissions.all() | Permission.objects.filter(group__user=self)
        return sorted([permission.codename for permission in permissions])
