from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from albums.serializers import AlbumSerializer, PhotoSerializer
from albums.models import Album, Photo


class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAuthenticated]
        return super(AlbumViewSet, self).get_permissions()

    def list(self, request, *args, **kwargs):
        pass

    def create(self, request, *args, **kwargs):
        user = request.user
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        pass

    def update(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        instance = Album.objects.get(id=pk)
        partial = kwargs.pop("partial", False)
        data = request.data
        serializer = self.serializer_class(instance, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class UploadPhoto(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = PhotoSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            album_id = kwargs["id"]
            data = request.data
            album = Album.objects.filter(id=album_id).first()
            serializer = self.serializer_class(data=data)
            if serializer.is_valid():
                serializer.save(album=album)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
