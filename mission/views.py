from rest_framework.viewsets import ModelViewSet

from user.models import User

from .models import Mission
from .serializers import MissionSerializer


class MissionViewSet(ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

    # def get_queryset(self):
    #     user = self.request.user
    #     if self.request.user.is_driver:
    #         return Mission.objects.filter(driver=user)
    #     else:
    #         return Mission.objects.all()
