from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from .views import MyView, TestViewSet

router = DefaultRouter()
router.register(r'my_view', MyView, basename='my_view', )


router_1 = SimpleRouter()

router_1.register(r'my_view2', TestViewSet, basename='my_view2', )


urlpatterns = [
    path('', include(router.urls)),
    path('test/', include(router_1.urls)),
]


