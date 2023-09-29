from rest_framework import generics
from rest_framework.permissions import AllowAny
from users.serializers import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Создание (регистрация) нового пользователя"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]  # added free user registration
