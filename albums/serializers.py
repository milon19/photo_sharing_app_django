from rest_framework import serializers

from albums.models import Album, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'photo']
        read_only_fields = ['id']


class AlbumSerializer(serializers.ModelSerializer):

    photos = PhotoSerializer(source='photo_album', read_only=True, many=True)
    author = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ['id', 'user', 'title', 'cover', 'is_private', 'created_at', 'updated_at', 'photos', 'author']
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']

    @staticmethod
    def get_author(obj):
        return obj.user.username
