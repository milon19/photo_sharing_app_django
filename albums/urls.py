from django.urls import path, include
from rest_framework.routers import DefaultRouter

from albums.views import GetOwnAlbum, AlbumViewSet

router = DefaultRouter()
router.register("albums", AlbumViewSet, basename="albums")

app_name = "albums"
urlpatterns = [
    path("", include(router.urls)),
    path("my-albums/<str:id>", GetOwnAlbum.as_view(), name="my-albums"),
]