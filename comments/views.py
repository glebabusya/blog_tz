from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from posts.permissions import IsAuthorOrReadOnly
from posts.utils import time_check
from . import models, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentListApiView(ListAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    def get(self, request, *args, **kwargs):
        time_check()
        return super(CommentListApiView, self).get(request, *args, **kwargs)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def get(self, request, *args, **kwargs):
        time_check()
        return super(CommentDetailAPIView, self).get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        time_check()
        return super(CommentDetailAPIView, self).put(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        time_check()
        return super(CommentDetailAPIView, self).delete(request, *args, **kwargs)


class CommentCreateAPIView(CreateAPIView):
    """
    Comment creation api view
    """
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        """
        method for saving comments
        """
        time_check()
        serializer = serializers.CommentCreateSerializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        comment = models.Comment(content=data['content'], author=request.user, post=data['post'])
        comment.save()
        return Response(
            status=status.HTTP_201_CREATED
        )
