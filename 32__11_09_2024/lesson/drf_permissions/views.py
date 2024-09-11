from django.db.models import QuerySet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Game, PaymentHistory
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from .serializers import *



class MyPermission(BasePermission):
    def has_permission(self, request, view):
        print(request)
        print(view)

        return True



class UserRegisterView(CreateAPIView):
    serializer_class = CreateUserSerializer
    queryset = User.objects.all()



class ProfileView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):

        serializer = ProfileSerializer(request.user)

        #print(request.user) #Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI1ODk4Mjc0LCJpYXQiOjE3MjU4OTc5NzQsImp0aSI6IjQ3OTljYWQ3OWEwOTRhNWJiNDU1MTUzYWU3MWNjMDgyIiwidXNlcl9pZCI6Mn0.gEaiLDokMCWdRhvgaqijXu8fijojK1fCq2mKTUikGS0

        return Response(data=serializer.data)



class GamesView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailView(RetrieveAPIView):
    queryset = Game.objects.all()
    serializer_class = GameInfoSerializer



class PaymentHistoryView(ListAPIView):

    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return PaymentHistory.objects.filter(user=self.request.user)

    serializer_class = PaymentHistorySerializer



class PaymentDepositView(CreateAPIView):

    permission_classes = (IsAuthenticated, )
    serializer_class = PaymentHistorySerializer


class LotsView(ListAPIView):
    serializer_class = LotsSerializer
    queryset = Lot.objects.all()

    def get_queryset(self):
        query = Lot.objects.raw("select *, count(id) as 'count' from drf_permissions_lot group by item_id ")
        return query