web: gunicorn blog_tz.wsgi
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate