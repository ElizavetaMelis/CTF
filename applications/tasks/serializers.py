from rest_framework import serializers

from applications.tasks.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_point = [i.point for i in instance.tasks.all()]
        if len(total_point) != 0:
            rep['total_point'] = sum(total_point)
        else:
            rep['total_point'] = 0
        return rep


