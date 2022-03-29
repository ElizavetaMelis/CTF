from rest_framework import serializers

from applications.testing.models import  Testing


# class LikeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Like
#         fields = '_all__'

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testing
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.user.id
        flag = Testing.objects.create(**validated_data)
        return flag

    # def to_representation(self, instance):
    #     rep = super().to_representation(instance)
    #     rep['user'] = f'{instance.user}'
    #     rep['like'] = instance.like.filter(like=True).count()
    #     return rep