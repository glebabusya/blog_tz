from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    content = models.CharField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content