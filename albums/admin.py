from django.contrib import admin

from albums.models import Album, Photo

admin.site.register(Album)
admin.site.register(Photo)
