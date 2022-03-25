from rest_framework import serializers

from applications.tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    flag = serializers.CharField(max_length=255)

    class Meta:
        model = Task
        fields = '__all__'

