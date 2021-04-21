FROM python:3.7

ENV PYTHONBUFFERED 1

WORKDIR /blog_tz

COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD python3 manage.py runserver 0.0.0.0:$PORT

