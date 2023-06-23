from rest_framework import serializers
from rest_framework.viewsets import ModelViewSet

from user.models import User

from .models import Mission
from .serializers import MissionSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_admin:
            return Mission.objects.all()
        else:
            return Mission.objects.filter(driver=user)
