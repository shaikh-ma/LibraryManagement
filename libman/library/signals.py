from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Request, Book


@receiver(post_save, sender=Request)
def create_request(sender, instance, created, **kwargs):
    if created:
        Request.objects.create(user=instance)


@receiver(post_save, sender=Request)
def save_request(sender, instance, **kwargs):
    # if hasattr(instance.request, 'is_approved'):
    #     instance.request.request_user = Book

    instance.request.save()