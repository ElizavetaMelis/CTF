from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from applications.testing.models import Testing
from applications.testing.serializers import TestingSerializer


class TestingViewSet(viewsets.ModelViewSet):
    queryset = Testing.objects.all()
    serializer_class = TestingSerializer
    permission_classes = [IsAuthenticated, ]
