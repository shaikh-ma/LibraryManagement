from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/home.html'
    context_object_name = 'books'
