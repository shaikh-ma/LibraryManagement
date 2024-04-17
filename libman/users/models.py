from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    roll_no = models.CharField(max_length=200)
    icard_no = models.CharField(max_length=200)
    class_div = models.CharField(max_length=200)
    # mobile_number = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Profile'