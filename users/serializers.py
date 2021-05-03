from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password",)
        extra_kwargs = {
            "password": {"write_only": True, "style": {"input_type": "password"}}
        }
        read_only_fields = ["id"]

    def create(self, validate_data):
        """Create a new user with hashed password"""
        user = get_user_model().objects.create_user(**validate_data)
        return user

    def update(self, instance, validated_data):
        """Hashing user password while update user info"""
        password = validated_data.pop("password", None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user