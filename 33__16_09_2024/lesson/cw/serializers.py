from django.contrib.auth.models import User
from rest_framework import serializers

from .models import *


class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, max_length=255)

    CHOISES = [
        ('0', 'Админ'),
        ('1', 'Продавец'),
        ('2', 'Покупатель')
    ]

    user_type = serializers.ChoiceField(choices=CHOISES)

    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'token', 'user_type')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UpdateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, max_length=255)

    class Meta:
        model = User
        fields = ('username', 'token')

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username')
        instance.save()
        return instance


class ListUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True, max_length=255)

    class Meta:
        model = User
        fields = ('username', 'token', )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        return Category.objects.create(**validated_data)


class UpdateCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')

    def update(self, instance, validated_data):
        print(instance)
        instance.name = validated_data.get('name')
        instance.save()
        return instance

