import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_tz.settings')

app = Celery('blog_tz')
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.update(BROKER_URL='redis://:p0e69cf0e29716269a48d4224ed645795505086a96a20465f14b9b1326fb65ee8@ec2-99-81-110-26.eu-west-1.compute.amazonaws.com:30359',
                CELERY_RESULT_BACKEND='redis://:p0e69cf0e29716269a48d4224ed645795505086a96a20465f14b9b1326fb65ee8@ec2-99-81-110-26.eu-west-1.compute.amazonaws.com:30359')

app.conf.beat_schedule = {
    'reset-upvotes-every-day': {
        'task': 'posts.tasks.reset_upvotes',
        'schedule': 60,
    },
}
