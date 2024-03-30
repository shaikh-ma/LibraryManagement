from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    book_id = models.IntegerField(primary_key = True)
    issued_to = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    return_date = models.DateField(blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.title

