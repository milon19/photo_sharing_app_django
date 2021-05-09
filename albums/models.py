import os
import uuid

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


def album_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/album/{}/'.format(instance.album.id), filename)


def cover_image_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('uploads/covers/{}/'.format(instance.user.username), filename)


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='album_user')
    title = models.CharField(max_length=100, blank=True, null=True)
    cover = models.ImageField(null=True, upload_to=cover_image_file_path, default="default_cover_pic.jpeg")
    is_private = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            this = Album.objects.get(id=self.id)
            if this.cover != self.cover:
                this.cover.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="photo_album")
    photo = models.ImageField(upload_to=album_image_file_path)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        try:
            this = Photo.objects.get(id=self.id)
            if this.photo != self.photo:
                this.photo.delete(save=False)
        except:
            pass  # when new photo then we do nothing, normal case
        super().save(*args, **kwargs)