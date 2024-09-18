from django.contrib.auth.models import User

from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CreateUserSerializer, UpdateUserSerializer, ListUserSerializer, CategorySerializer, UpdateCategorySerializer


def nothing(x):
    return x


class UserRegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()


class ProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        nothing(self)
        return Response({'user': request.user.username})


class EditProfileView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, request):
        nothing(self)
        serializer = UpdateUserSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


class ListUsersView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListUserSerializer
    queryset = User.objects.all()


class CategoryListView(ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CreateCategoryView(CreateAPIView):

    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class EditCategoryView(APIView):
    # permission_classes = (IsAuthenticated,)

    def put(self, request):
        print(request.data)
        nothing(self)
        category = Category.objects.get(pk=request.data['id'])

        serializer = UpdateCategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)