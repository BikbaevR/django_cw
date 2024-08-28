from django.urls import path
from .views import *

urlpatterns = [
    # path('test/', TestView.as_view(), name='test'),
    # path('test/v2/', GetPostListGeneric.as_view(), name='testv2'),
    # path('test/v2/create/', GetPostListGenericNew.as_view(), name='testv2create'),
    # path('test/v2/create1/', GetPostListGenericNew1.as_view(), name='testv2create1'),
    #
    # path('test/v2/create2/', GetPostListGenericNew2.as_view(), name='testv2create2'),
    # path('test/v2/create2/<int:pk>', GetPostListGenericNew2.as_view(), name='testv2create2'),

    path('test/v2/', GetPostListGeneric.as_view(), name='two'),
    path('test/v2/<int:pk>', GetPostById.as_view(), name='three'),
    path('test/v2/delete/<int:pk>', PostDeleteById.as_view(), name='four'),
    path('test/v2/update/<int:pk>', PostUpdateById.as_view(), name='four'),

]