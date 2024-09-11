from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from .serializers import CreateUserSerializer



class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print(request)
        print(view)

        return True



class UserRegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()



class ProfileView(APIView):

    permission_classes = (IsAuthenticated, MyPermission)

    def get(self, request):
        print(request.user) #Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODk4Mjc0LCJpYXQiOjE3MjU4OTc5NzQsImp0aSI6IjQ3OTljYWQ3OWEwOTRhNWJiNDU1MTUzYWU3MWNjMDgyIiwidXNlcl9pZCI6Mn0.gEaiLDokMCWdRhvgaqijXu8fijojK1fCq2mKTUikGS0

        return Response(data={'username': request.user.username})
