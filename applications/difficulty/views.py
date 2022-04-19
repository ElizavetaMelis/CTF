from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from applications.difficulty.models import Difficulty
from applications.difficulty.permissions import IsSuperUser
from applications.difficulty.serializers import DifficultySerializer


class DifficultyViewSet(viewsets.ModelViewSet):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes = [IsAuthenticated, IsSuperUser]

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = ''
        else:
            permissions = [IsAuthenticated, IsSuperUser]
        return [permission() for permission in permissions]


