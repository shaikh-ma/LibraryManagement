FROM python:3.10

EXPOSE 8000

WORKDIR /app

COPY . .

EXPOSE 8080

RUN pip install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

CMD ["python", "manage.py", "runserver"]
