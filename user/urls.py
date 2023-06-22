from django.urls import include, path
from rest_framework import routers

from user import views

app_name = "user"

router = routers.SimpleRouter()
router.register("users", views.UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]
