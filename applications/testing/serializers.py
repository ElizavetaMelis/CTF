from rest_framework import serializers

from applications.testing.models import  Testing

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        flag = Testing.objects.create(**validated_data)
        return flag
