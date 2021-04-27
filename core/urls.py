from django.urls import path
from core.views import HomePage

app_name = "core"

urlpatterns = [
    path("homepage/", HomePage.as_view(), name="homepage")
]