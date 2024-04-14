from django.contrib import admin
from .models import Book, Request, ReturnRequest

# Register your models here.
admin.site.register(Book)
admin.site.register(Request)
admin.site.register(ReturnRequest)