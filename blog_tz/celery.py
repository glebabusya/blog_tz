import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_tz.settings')

app = Celery('blog_tz')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'reset-upvotes-every-day': {
        'task': 'posts.tasks.reset_upvotes',
        'schedule': 60,
    },
}
