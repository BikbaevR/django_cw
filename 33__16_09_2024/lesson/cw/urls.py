from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import *



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('update_user/', EditProfileView.as_view(), name='update_user'),
    path('list_user/', ListUsersView.as_view(), name='list_user'),
    path('category_list/', CategoryListView.as_view(), name='category_list'),
    path('create_category/', CreateCategoryView.as_view(), name='create_category'),
    path('edit_category/', EditCategoryView.as_view(), name='edit_category'),

]