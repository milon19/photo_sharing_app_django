from rest_framework.serializers import ModelSerializer

from profiles.models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "user", "name", "profile_pic", "phone", "created_at", "updated_at", "profile_setup", ]
        read_only_fields = ["id", "profile_pic", "profile_setup", "created_at", "updated_at", "user"]
