from django.contrib.auth import get_user_model

from rest_framework import viewsets, status
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from profiles.models import Profile
from profiles.serializers import ProfileSerializer
from core.permissions import UpdateOwnProfile
from users.serializers import UserWithProfileSerializer

User = get_user_model()


class ProfileViewSet(viewsets.GenericViewSet, RetrieveModelMixin):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def get_permissions(self):
        if self.action in ["update"]:
            self.permission_classes = [IsAuthenticated, UpdateOwnProfile]
        else:
            self.permission_classes = [AllowAny]
        return super(ProfileViewSet, self).get_permissions()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs["pk"]
        user = self.queryset.filter(id=pk).first().user
        serializer = ProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        pk = kwargs["pk"]
        instance = Profile.objects.get(id=pk)
        data = request.data

        profile_setup = True if data.get("profile_setup") == "true" else False

        serializer = self.serializer_class(instance, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save(
                profile_setup=profile_setup,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return self.update(request, *args, **kwargs)


class GetOwnProfile(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserWithProfileSerializer

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            qs = User.objects.filter(id=user.id).first()
            serializer = self.serializer_class(qs)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "Authentication credentials were not provided."},
            status=status.HTTP_401_UNAUTHORIZED,
        )
