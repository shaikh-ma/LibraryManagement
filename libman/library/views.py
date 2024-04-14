from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Book, Request, ReturnRequest
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render, redirect
from .forms import RequestForm, ReturnRequestForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

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
    if request.method == "POST":
        form = RequestForm(request.POST)
        if request.user.is_superuser:
            messages.success(request, f'Admin cannot request book!')
            return redirect('user-requests', username=request.user)
        
        if form.is_valid():
            book_title = form.cleaned_data['request_book']
            book_details = Book.objects.filter(title=book_title).values()[0]
            book_request = form.save(commit=False)
            book_request.request_user = request.user
            book_request.request_book_title = book_details['title']
            book_request.request_book_code = book_details['book_code']
            book_request.request_date = timezone.now()

            book_request.save()
            messages.success(request, f'Your request has been created!')
            return redirect('user-requests', username=request.user)
    else:
        form = RequestForm()
    return render(request, 'library/requests.html', {'form': form})



class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class RequestDetailView(DetailView):
    model = Request
    template_name = 'library/request_detail.html'
    context_object_name = 'request'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context





class UserReturnRequestsListView(ListView):
    model = ReturnRequest
    template_name = 'library/user_return_requests.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'requests'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Request.objects.filter(request_user=user)



@login_required
def request_book_return(request, bookid):
    if request.method == "POST":
        form = ReturnRequestForm(request.POST)
        if request.user.is_superuser:
            messages.success(request, f'Admin cannot return a book!')
            return redirect('home')
        
        if form.is_valid():
            book_details = Book.objects.filter(pk=bookid).values()[0]
            book_request = form.save(commit=False)
            book_request.request_user = request.user
            book_request.request_date = timezone.now()
            book_request.request_book_title = book_details['title'] 
            book_request.request_book_code = book_details['book_code']
            book_request.is_approved = False
            book_request.save()
            messages.success(request, f'Your request has been created!')
            return redirect('user-return-requests', username=request.user)
    else:
        form = ReturnRequestForm()
    return render(request, 'library/return_requests.html', {'form': form})

