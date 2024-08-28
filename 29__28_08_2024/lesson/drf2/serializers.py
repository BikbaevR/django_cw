from rest_framework import serializers

from .models import *


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data): #instance - объект модели
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.save()
        return instance


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = ('id', 'title', 'content')
        fields = '__all__'
        # exclude = ['id']
        read_only_fields = ('id',)
