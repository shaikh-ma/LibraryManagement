from django.views.generic import ListView
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
# Create your views here.

class BookListView(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'library/home.html'
    context_object_name = 'books'


class UserBooksListView(ListView):
    model = Book
    template_name = 'library/user_books.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Book.objects.filter(issued_to=user)