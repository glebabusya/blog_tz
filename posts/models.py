from django.db import models, IntegrityError
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=63)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvote_amount = models.IntegerField(default=0)
    content = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="posts")

    def __str__(self):
        return self.title

    def upvote(self, user):
        """
        Method for upvote posts. User must be authenticated
        """
        self.upvote_amount = Upvote.objects.filter(post=self).count()
        try:
            Upvote.objects.get(user=user, vote=self)
            return None
        except Exception as e:
            try:
                vote = Upvote(user=user, post=self)
                vote.save()
                self.upvote_amount += 1
                self.save()
            except IntegrityError:
                return None


class Upvote(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="upvote")
    post = models.ForeignKey(to=Post, related_name="upvotes", on_delete=models.CASCADE)

    class Meta:
        unique_together = ("user", "post")
