from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer

from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics

from rest_framework.permissions import IsAuthenticatedOrReadOnly

# class PostListCreateAPIView(APIView):
#
#     # def get(self, request):
#     #     posts = Post.objects.all()
#     #     serializer = PostSerializer(posts, many=True)
#     #     return Response(serializer.data)
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
#
# class PostDetailAPIView(APIView):
#
#     def get_object(self, pk):
#         return Post.objects.get(pk=pk)
#
#     def get(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         post = self.get_object(pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors)
#
#     def delete(self, request, pk):
#         post = self.get_object(pk)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

@extend_schema(tags=['Post'])
class PostViewSetApiView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PostCreateApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
