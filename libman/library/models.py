from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    user_issued = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

