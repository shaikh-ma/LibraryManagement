FROM python:slim as python

WORKDIR ./app

COPY ./libman ./app

CMD ['python', 'manage.py' , 'runserver']

