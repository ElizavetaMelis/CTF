from rest_framework import status, generics, filters, viewsets
from rest_framework.pagination import PageNumberPagination
from django_filters import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.account.models import Profile
from applications.tasks.models import Task
from applications.tasks.permissions import IsSuperUser
from applications.tasks.serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend

class TaskFilter(rest_framework.FilterSet):
    difficulty = rest_framework.NumberFilter(field_name='difficulty')
    category = rest_framework.NumberFilter(field_name='category')
    class Meta:
        model = Task
        fields = ['difficulty',
                  'category',
                  ]

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsSuperUser]
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filter_class = TaskFilter
    search_fields = ['category', 'description', ]

    def get_serializer_context(self):
        return {'request': self.request}

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permissions = ''
        else:
            permissions = [IsAuthenticated, IsSuperUser]
        return [permission() for permission in permissions]



class TaskDetailView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class FavoriteView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request, pk):
        profile = Profile.objects.get(user=request.user.id)
        if profile.favorite.filter(id=pk).exists():
            profile.favorite.set(profile.favorite.exclude(id=pk))
            msg = 'Task was deleted from favorites!'
        else:
            profile.favorite.add(pk)
            profile.save()
            msg = 'Task added to favorite successfully!'
        return Response(msg, status=status.HTTP_200_OK)