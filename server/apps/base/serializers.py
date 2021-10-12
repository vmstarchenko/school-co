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


class BaseUploadedFileSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    url = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    uid = serializers.SerializerMethodField(method_name='get_url')
    status = serializers.ReadOnlyField(default='done')

    def get_url(self, obj):
        return self.context['request'].build_absolute_uri(obj.file.url)

    def get_name(self, obj):
        return os.path.basename(obj.file.url)

    class Meta:
        fields = ['id', 'url', 'name', 'uid', 'status']
