from django.views.generic import ListView, CreateView
from django.contrib import messages
from .models import Book, Request
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RequestForm
from django.contrib.auth.decorators import login_required


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

class UserRequestsListView(ListView):
    model = Request
    template_name = 'library/user_requests.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'requests'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Request.objects.filter(request_user=user)


@login_required
def new_request(request):
    user = request.user

    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.request_user = user
            obj.save()
            messages.success(request, f'Your request has been created!')
            return redirect('home')
    form = RequestForm()
    return render(request, 'library/requests.html', {'form': form})
