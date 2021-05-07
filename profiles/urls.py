from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles.views import ProfileViewSet, GetOwnProfile

router = DefaultRouter()
router.register("profiles", ProfileViewSet, basename="profiles")

app_name = "profiles"
urlpatterns = [
    path("", include(router.urls)),
    path("profiles/", GetOwnProfile.as_view(), name="my-profile"),
]