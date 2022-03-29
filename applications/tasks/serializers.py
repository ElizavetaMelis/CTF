from rest_framework import serializers

from applications.tasks.models import TaskImage, Task


class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image', )

    def _get_image_url(self, obj):
        if obj.image:
            url = obj.image.url
            request = self.context.get('request')
            if request is not None:
                url = request.build_absolute_uri(url)
        else:
            url = ''
        return url

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['image'] = self._get_image_url(instance)
        return rep

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        total_rating = [i.rating for i in instance.testing.all()]
        if len(total_rating) != 0:
            rep['total_rating'] = sum(total_rating) / len(total_rating)
        else:
            rep['total_rating'] = ''
        rep['images'] = TaskImageSerializer(TaskImage.objects.filter(task=instance.id), many=True, context=self.context).data
        return rep

