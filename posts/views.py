from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from . import models, serializers, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.models import User


class PostListAPIView(ListCreateAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        serializer = serializers.PostSerializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        post = models.Post(title=data['title'], content=data['content'], author=request.user)
        post.save()
        return Response(
            status=status.HTTP_201_CREATED
        )


class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, permissions.IsAuthorOrReadOnly]
