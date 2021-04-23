FROM python:3.7

ENV PYTHONBUFFERED 1

WORKDIR /usr/src/app

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install -r requirements.txt
RUN chmod +x entrypoint.sh

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]