from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.

class BookListView(ListView):
    model = Book
    template_name = 'library/index.html'
    context_object_name = 'books'
