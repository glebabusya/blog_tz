from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from . import models, serializers, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)

from .utils import time_check


class PostListAPIView(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        time_check()
        return super(PostListAPIView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        method for saving posts
        """
        time_check()
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        post = models.Post(
            title=data["title"], content=data["content"], author=request.user
        )
        post.save()
        return Response(status=status.HTTP_201_CREATED)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        time_check()
        return super(PostDetailAPIView, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        time_check()
        return super(PostDetailAPIView, self).put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        time_check()
        return super(PostDetailAPIView, self).delete(request, *args, **kwargs)


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def upvote(request, pk):
    time_check()
    try:
        post = models.Post.objects.get(pk=pk)
        post.upvote(request.user)
        return redirect("post_detail", pk)
    except models.Post.DoesNotExist:
        return redirect("post_detail", pk)
