from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from albums.serializers import AlbumSerializer
from albums.models import Album


class GetOwnAlbum(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AlbumSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            album_id = kwargs['id']
            user = request.user
            qs = Album.objects.filter(id=album_id).first()

            if user.id != qs.user.id:
                return Response(
                    {"detail": "Authentication credentials were not provided."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            serializer = self.serializer_class(qs)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )

