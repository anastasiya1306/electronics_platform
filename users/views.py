from rest_framework import generics

from users.models import User, UserRoles
from users.serializers import UserSerializer, AuthUserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """Отображение списка пользователей"""
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AuthUserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        """Отображение деталей пользователя с проверкой прав доступа"""
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Обновление пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser or user.role == UserRoles.MODERATOR:
            return User.objects.all()
        else:
            return User.objects.filter(pk=user.id)
