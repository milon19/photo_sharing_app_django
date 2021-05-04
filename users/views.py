from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from users.serializers import UserRegistrationSerializer


class CreateUserView(CreateAPIView):
    """Create a new user in the system"""

    permission_classes = [
        AllowAny,
    ]
    serializer_class = UserRegistrationSerializer