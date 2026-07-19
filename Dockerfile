FROM python:slim

WORKDIR /app

COPY ./libman /app

CMD ['python', 'manage.py' , 'runserver']

