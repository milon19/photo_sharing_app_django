from django.urls import path, include
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]