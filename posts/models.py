from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=63)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote_amount = models.PositiveIntegerField(default=1)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='posts')

    def upvote(self):
        """
        Method for increasing upvotes
        """
        self.upvote_amount += 1
        self.save()

    def __str__(self):
        return self.title