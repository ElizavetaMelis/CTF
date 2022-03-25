from rest_framework import generics

from applications.difficulty.models import Difficulty
from applications.difficulty.serializers import DifficultySerializer


class DifficultyListView(generics.ListAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer

