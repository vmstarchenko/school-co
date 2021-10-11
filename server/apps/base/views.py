from django.contrib.auth import authenticate

from drf_spectacular.utils import extend_schema

from rest_framework import status, serializers, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, FullUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    class LoginFormSerializer(serializers.Serializer):
        username = serializers.CharField()
        password = serializers.CharField()

    class EmptySerializer(serializers.Serializer):
        pass

    @extend_schema(
        request=LoginFormSerializer,
        operation_id='user_login',
        responses={
            200: FullUserSerializer
        },
    )
    @action(
        detail=False,
        methods=['POST'],
        permission_classes=[AllowAny],
    )
    def login(self, request):
        print(request.__dict__)
        print('r', request.GET, request.POST, request.data)
        form = self.LoginFormSerializer(data=request.data)
        if not form.is_valid():
            return Response({
                'status': 'Authentication failed',
            }, status=status.HTTP_401_UNAUTHORIZED)

        user = authenticate(request, **form.data)
        if user is None:
            return Response({
                'status': 'Authentication failed',
            }, status=status.HTTP_401_UNAUTHORIZED)

        Token.objects.get_or_create(user=user)

        data = FullUserSerializer(user, context={'request': self.request}).data
        return Response(data)

    @extend_schema(request=EmptySerializer, operation_id='user_logout')
    @action(detail=False, methods=['post'])
    def logout(self, request):
        # pylint: disable=no-self-use

        return Response({
            'success': 'You have successfully logged out',
        })

    @extend_schema(
        operation_id='user_me',
        request=EmptySerializer,
        responses={
            200: FullUserSerializer
        },
    )
    @action(detail=False, methods=['get'], permission_classes=[AllowAny])
    def me(self, request):
        # pylint: disable=no-self-use
        return Response(FullUserSerializer(
            request.user,
            context={'request': request},
        ).data)
