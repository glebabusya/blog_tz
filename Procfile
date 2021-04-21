web: gunicorn blog_tz.wsgi
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
worker: celery worker -A blog_tz --loglevel=info
channelsworker: python manage.py runworker -v2
