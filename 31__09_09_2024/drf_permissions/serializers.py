from .models import User
from rest_framework import serializers


class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'token']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
