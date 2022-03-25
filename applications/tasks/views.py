from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from applications.tasks.serializers import TaskSerializer


class TaskView(APIView):
    def post(self, request):
        data = request.data
        serializer = TaskSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registration!', status = status.HTTP_201_CREATED)
