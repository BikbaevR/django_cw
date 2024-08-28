from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView, RetrieveAPIView, DestroyAPIView, \
    UpdateAPIView

from .models import *

from .serializers import *


def nothing(x):
    return x


class TestView(APIView):

    def get(self, request):
        nothing(self)
        # data = [
        #     {
        #         'value': Post.objects.all().values()
        #     }
        # ]
        # return Response(data)

        data = Post.objects.all()
        serializer = ModelSerializer(data, many=True)
        return Response({
            'data': serializer.data,
            'status_code': status.HTTP_200_OK
        })

    def post(self, request):
        nothing(self)
        # title = request.data['title']
        # content = request.data['content']


        # new_post = Post.objects.create(title=title, content=content)

        # data = [{
        #     'value': model_to_dict(new_post),
        # }]

        # return Response(data)
        # return Response(PostSerializer(new_post).data)

        serializer = ModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save(user=request.data['user'])
            serializer.save()
            return Response(serializer.data)
        return Response({'error': 'error'})

    def put(self, request):
        nothing(self)

        instance = Post.objects.get(pk=request.data['id'])

        serializer = ModelSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)#для того что бы в ответ возвращалась ошибка если она есть
        serializer.save()
        return Response(serializer.data)




# class GetPostListGeneric(ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ModelSerializer
#
#
# class GetPostListGenericNew(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ModelSerializer
#
# class GetPostListGenericNew1(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ModelSerializer




# class GetPostListGenericNew2(RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = ModelSerializer


class GetPostListGeneric(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = ModelSerializer


class GetPostById(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = ModelSerializer

class PostDeleteById(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = ModelSerializer

class PostUpdateById(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = ModelSerializer