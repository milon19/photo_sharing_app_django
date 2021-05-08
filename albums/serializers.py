from rest_framework import serializers

from albums.models import Album, Photo


# from users.serializers import UserWithProfileSerializer


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo']
        read_only_fields = ['id']


class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(source='photo_album', read_only=True, many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'cover', 'is_private', 'created_at', 'updated_at', 'photos']
        read_only_fields = ['id', 'created_at', 'updated_at']
