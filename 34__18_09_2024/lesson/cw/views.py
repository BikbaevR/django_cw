from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializers import TestSerializer
from rest_framework.decorators import action

from .models import Test

# Create your views here.


class MyView(ModelViewSet):
    serializer_class = TestSerializer
    queryset = Test.objects.all()



class TestViewSet(ViewSet):

    @action(methods=['get'], detail=False)
    def list_method(self, request, *args, **kwargs):
        print('list')
        return Response('list')

    def retrieve(self, request, pk=None):
        print('retrieve')
        return Response('retrieve')

    def create(self, request):
        print('create')
        return Response('create')

    def destroy(self, request, pk=None):
        print('destroy')
        return Response('destroy')
