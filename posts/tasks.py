import logging
from blog_tz.celery import app
from posts.models import Upvote


@app.task
def reset_upvotes():
    Upvote.objects.all().delete()