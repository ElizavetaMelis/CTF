from rest_framework import serializers

from applications.difficulty.models import Difficulty


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = '__all__'

