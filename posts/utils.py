from django.utils import timezone
import datetime

from . import models


def delete_upvotes():
    models.Upvote.objects.all().delete()


def time_check():
    """
    This function is needed to delete upvotes every 24 hours
    """
    # This is a crutch, you need to use Celery

    delete_time = models.DeleteUpvote.objects.last().time
    now = timezone.now()
    t_delta = (now - delete_time).total_seconds()
    if t_delta >= 86400:
        delete_upvotes()
        delete_time = datetime.datetime(
            year=now.year, month=now.month, day=now.day, hour=0, minute=0, second=1
        )
        models.DeleteUpvote(time=delete_time).save()
