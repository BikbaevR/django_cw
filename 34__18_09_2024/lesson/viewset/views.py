from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet, ModelViewSet


class MyViewSet(ViewSet):

    @action(methods=['get'], detail=True)
    def my_request(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        return Response({'message': 'Hello World'})

    def list(self, request, *args, **kwargs):
        return Response({'method': 'list'})

    def retrieve(self, request, pk=None, *args, **kwargs):
        return Response({'method': 'retrieve' + ' ' + pk})

    def destroy(self, request, pk=None, *args, **kwargs):
        return Response({'method': 'destroy' + ' ' + pk})


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class MyModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request, *args, **kwargs):
        return Response({'method': 'list'})
