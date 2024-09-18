from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()
router.register(r'test', MyViewSet, basename='test', )
router.register(r'test1', MyModelViewSet, basename='test1', )

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
