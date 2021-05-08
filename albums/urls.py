from django.urls import path

from albums.views import GetOwnAlbum

app_name = "albums"
urlpatterns = [
    path("my-albums/<str:id>", GetOwnAlbum.as_view(), name="my-albums"),
]