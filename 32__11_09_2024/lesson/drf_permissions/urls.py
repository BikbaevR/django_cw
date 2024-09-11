from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('games/', GamesView.as_view(), name='games'),
    path('games/<int:pk>', GameDetailView.as_view(), name='gameDetail'),
    path('payment-history/', PaymentHistoryView.as_view(), name='paymentHistory'),
    path('payment/deposit/', PaymentDepositView.as_view(), name='paymentDeposit'),
    path('lots/', LotsView.as_view(), name='lots'),
]