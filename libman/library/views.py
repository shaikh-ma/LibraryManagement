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
            book_id = form.cleaned_data['request_book_code']
            try:
                book_details = Book.objects.filter(book_code=book_id).values()[0]
            except IndexError:
                err = "Book code '{}' does not exists!".format(book_id)
                messages.error(request, err)
                return redirect('home')

            if not book_details['is_available']:
                err = "Book not available"
                messages.error(request, err)
                return redirect('home')

            existing = Request.objects.filter(request_book_code=book_details['book_code'])
            if len(existing.values()):
                err = "Request already exists!"
                messages.error(request, err)
                return redirect('home')

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
    context_object_name = 'ret_requests'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ReturnRequest.objects.filter(request_user=user)



@login_required
def request_book_return(request, bookid):
    if request.method == "POST":
        form = ReturnRequestForm(request.POST)
        if request.user.is_superuser:
            messages.success(request, f'Admin cannot return a book!')
            return redirect('home')

        if form.is_valid():
            book_request = form.save(commit=False)
            book_details = Book.objects.get(pk=bookid)
            existing = ReturnRequest.objects.filter(request_book_code=book_details.book_code)
            if len(existing.values()):
                err = "Request already exists!"
                messages.error(request, err)
                return redirect('home')

            book_request.request_book_code = book_details.book_code
            book_request.request_book_title = book_details.title
            book_request.request_user = request.user
            book_request.is_raised = True
            book_request.save()
            messages.success(request, f'Your request has been created!')
            return redirect('user-return-requests', username=request.user)
    else:
        form = ReturnRequestForm()
    return render(request, 'library/return_requests.html', {'form': form})


def about_page(request):
    return render(request, 'library/about.html')