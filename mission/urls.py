from django.urls import include, path
from rest_framework import routers

from mission import views

app_name = "mission"

router = routers.SimpleRouter()
router.register("missions", views.MissionViewSet, basename="missions")

urlpatterns = [
    path("", include(router.urls)),
]
