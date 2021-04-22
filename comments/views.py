from django.shortcuts import redirect
from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
)
from rest_framework.response import Response
from posts.permissions import IsAuthorOrReadOnly
from . import models, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class CommentListApiView(ListAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


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
        serializer = serializers.CommentCreateSerializer(data=request.data)
        serializer.is_valid()
        data = serializer.validated_data
        comment = models.Comment(
            content=data["content"], author=request.user, post=data["post"]
        )
        comment.save()
        return redirect('comment_detail', comment.pk)
