from celery import shared_task
from blog_tz.celery import app
from posts.models import Upvote, Post


@shared_task
def reset_upvotes():
    Upvote.objects.all().delete()
    posts = Post.objects.all()
    for post in posts:
        post.reset_upvote()

    return "Upvote Deleted"
