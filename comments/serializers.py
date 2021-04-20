from rest_framework import serializers

from posts.models import Post
from . import models


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.HyperlinkedRelatedField(view_name='post_detail', read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='comment_detail')

    class Meta:
        model = models.Comment
        fields = [
            'content', 'author', 'post', 'creation_date', 'link'
        ]


class CommentCreateSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)

    class Meta:
        model = models.Comment
        fields = [
            'content', 'author', 'post', 'creation_date'
        ]
