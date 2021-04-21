import logging

from celery import shared_task

from blog_tz.celery import app
from posts.models import Upvote


@shared_task
def reset_upvotes():
    Upvote.objects.all().delete()
    return 'Upvotes Deleted'