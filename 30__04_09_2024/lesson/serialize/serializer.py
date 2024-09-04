from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Post, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Post
        fields = '__all__'
        # depth = 1


class PostObjectSerializer(serializers.ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Post
        fields = '__all__'


class CategoryListSerializer(serializers.ModelSerializer):
    posts = PostObjectSerializer(many=True)

    class Meta:
        model = Category
        fields = '__all__'


