# from django.urls import path
# from .views import PostListCreateAPIView, PostDetailAPIView
#
# urlpatterns = [
#     path('posts/', PostListCreateAPIView.as_view()),
#     path('posts/<int:pk>/', PostDetailAPIView.as_view()),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSetApiView

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('posts', PostViewSetApiView)

urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', obtain_auth_token),
]