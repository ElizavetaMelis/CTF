from rest_framework import viewsets, permissions

from rest_framework.permissions import IsAuthenticated

from applications.category.models import Category
from applications.category.permissions import IsSuperUser
from applications.category.serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsSuperUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = ''
        else:
            permissions = [IsAuthenticated, IsSuperUser]
        return [permission() for permission in permissions]

