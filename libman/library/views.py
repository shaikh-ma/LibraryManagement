from django.shortcuts import render
from .models import Book
# Create your views here.

def index(request):
    all_books = Book.objects.all()
    context = {"books": all_books}
    return render(request, "library/index.html", context)

def add_book(request):
    context = {"context": request.form}
    print(context)
    return render(request, "library/index.html", context)