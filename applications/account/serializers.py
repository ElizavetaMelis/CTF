import serializers as serializers
from django.contrib.auth import get_user_model, authenticate
from rest_framework import serializers

from applications.account.models import Profile
from applications.account.utils import send_activation_email

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('fullname', 'email', 'password', 'password_confirmation')

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('User already exists')
        return email

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Password error')
        return validated_data

    def create(self, validated_data):
        fullname = validated_data.get('fullname')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = User.objects.create_user(fullname, email, password)
        profile = Profile.objects.create(user_id=user.id)
        send_activation_email(user.email, user.activation_code)
        return profile

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'), username=email, password=password)
            if not user:
                msg = 'No login with provided credentials'
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = 'No "password" or "email"'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return attrs

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
