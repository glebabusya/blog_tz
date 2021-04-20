from rest_framework import serializers
from . import models
from django.contrib.auth.models import User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    upvote_amount = serializers.IntegerField(read_only=True)
    link = serializers.HyperlinkedIdentityField(view_name='post_detail')
    upvote = serializers.HyperlinkedIdentityField(view_name='upvote', lookup_field='pk')

    class Meta:
        model = models.Post
        fields = [
            'id', 'title', 'author', 'content', 'upvote_amount', 'creation_date', 'link', 'upvote'
        ]
