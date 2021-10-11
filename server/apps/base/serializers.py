from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers

from .models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'id', 'url',
            'username',
            'email',
        ]


class FullUserSerializer(UserSerializer):
    permissions = serializers.SerializerMethodField()
    token = serializers.SerializerMethodField()

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + [
            'permissions',
            'token',
        ]

    @extend_schema_field(str)
    def get_token(self, request):
        return self.instance.token

    @extend_schema_field(serializers.ListField(child=serializers.CharField()))
    def get_permissions(self, request):
        return sorted(self.instance.get_all_permissions())
