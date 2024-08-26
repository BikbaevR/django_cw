from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *


#pip install djangorestframework

posts = []


class GetPostListView(APIView):
    def get(self, request):
        data = [{
            'data': Post.objects.all().values(),
            'status': 200
        }]

        return Response(data)

    # def post(self, request):
    #     posts.append({
    #         'id': request.data['id'],
    #         'title': request.data['title'],
    #         'content': request.data['content'],
    #     })
    #
    #     data = [{
    #         'data': posts,
    #         'status': 201
    #     }]
    #
    #     return Response(data)

    def post(self, request):
        post = Post.objects.create(
            title=request.data['title'],
            content=request.data['content'],
        )

        data = [{
            'data': model_to_dict(post),
            'status': 201
        }]

        return Response(data)


class GetPostDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        #http://127.0.0.1:8000/api/v1/test/15?name=12345&fillter=1
        print(request.query_params)
        print(pk)
        data = [{
            'data': posts,
            'status': 200
        }]

        return Response(data)
