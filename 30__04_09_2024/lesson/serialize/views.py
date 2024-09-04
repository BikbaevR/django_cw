from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Post, Category
from .serializer import PostSerializer, CategoryListSerializer


class GetPostListView(ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()


class GetCategoryList(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer
