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


class PostListAPIView(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        """
        method for saving posts
        """
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        post = models.Post(
            title=data["title"], content=data["content"], author=request.user
        )
        post.save()
        return redirect('post_detail', post.pk)


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly]


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def upvote(request, pk):
    try:
        post = models.Post.objects.get(pk=pk)
        post.upvote(request.user)
        return redirect("post_detail", pk)
    except models.Post.DoesNotExist:
        return redirect("post_detail", pk)
