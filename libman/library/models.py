from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    book_id = models.IntegerField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_available = models.BooleanField(default=True)
    issued_date = models.DateField(blank=True, null=True)
    returned_date = models.DateField(blank=True, null=True)
    date_book_added = models.DateField(default=timezone.now)
    book_code = models.CharField(max_length=300)
    summary = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title


class Request(models.Model):
    request_id = models.IntegerField(primary_key=True, auto_created=True)
    request_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    request_book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=True, null=True)
    request_date = models.DateField(auto_now=True)
    return_date = models.DateField(default=timezone.now())
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return "{} - {} - {}".format(
            self.request_id,
            self.request_user,
            self.request_book
        )