from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from library.models import Book, Request, User, ReturnRequest
from django.contrib import messages
from django.utils import timezone
from library.forms import BookForm, BookEditForm

from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.management import call_command

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def library_admin(request):
    return render(request, 'libadmin/admin.html')


@user_passes_test(is_admin)
def manage_books(request):
    books = Book.objects.all()
    return render(request, 'libadmin/manage_books.html', {'books': books})

@user_passes_test(is_admin)
def manage_requests(request):
    requests = Request.objects.all()
    return render(request, 'libadmin/manage_requests.html', {'requests': requests})

@user_passes_test(is_admin)
def manage_return_requests(request):
    requests = ReturnRequest.objects.all()
    return render(request, 'libadmin/manage_return_requests.html', {'requests': requests})

@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    books = Book.objects.filter()
    return render(request, 'libadmin/manage_users.html', {'users': users, 'books': books})


@user_passes_test(is_admin)
def delete_book(request, bookid):
    book = Book.objects.get(pk=bookid)
    if book.issued_to:
        msg = "Cannot delete a book issued to a user"
        messages.error(request, msg)
    else:
        book.delete()
        msg = "'{}' Book has been deleted!".format(book.title)
        messages.success(request, msg)
    return redirect('home')


@user_passes_test(is_admin)
def delete_request(request, rqid):
    user_req = Request.objects.get(pk=rqid)
    user_req.delete()
    msg = "Request has been deleted!"
    messages.success(request, msg)
    return redirect('home')


@user_passes_test(is_admin)
def delete_user(request, rqid):
    user = User.objects.get(pk=rqid)
    user.delete()
    msg = "User has been deleted!"
    messages.success(request, msg)
    return redirect('home')


@user_passes_test(is_admin)
def add_new_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if not request.user.is_superuser:
            messages.success(request, f'Only Admins can add book!')
            return redirect('user-requests', username=request.user)
        
        if form.is_valid():
            form.save()
            messages.success(request, f'Book as been added')
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'libadmin/add_new_book.html', {'form': form})


@user_passes_test(is_admin)
def edit_book(request, bookid):
    if request.method == "POST":
        form = BookEditForm(request.POST)
        if form.is_valid():
            book_form = form.save(commit=False)
            book_details = form.cleaned_data
            book = Book.objects.get(pk=bookid)
            book.title = book_details['title']
            book.author = book_details['author']
            book.summary = book_details['summary']
            book_form.save()
            book.save(update_fields=["title", "author", "summary"])
            messages.success(request, f'Book as been added')
            return redirect('home')
    else:
        form = BookEditForm()
    return render(request, 'libadmin/edit_book.html', {'form': form})


@user_passes_test(is_admin)
def approve_book_return(request, rqid):
    user_req = ReturnRequest.objects.get(pk=rqid)
    if not user_req.is_approved:
        user_req.is_approved = True
        book = Book.objects.get(code=user_req.request_book_code)
        book.issued_to = None
        book.returned_date = None
        book.issued_date = None
        book.is_available = True
        book.save()
        user_req.save()
        msg = "Request Approved! Book issued to {}".format(user_req.request_user)
        messages.success(request, msg)
        user_req.delete()
    return redirect('home')


@user_passes_test(is_admin)
def confirm_return(request, rqid):
    user_req = ReturnRequest.objects.get(pk=rqid)
    if not user_req.is_approved:
        book = Book.objects.get(book_code=user_req.request_book_code)
        if book:
          user_req.is_approved = True
          book.issued_to = None
          book.returned_date = None
          book.issued_date = None
          book.is_available = True
          book.save()
          user_req.save()
          msg = "Book return is confirmed"
          messages.success(request, msg)
          user_req.delete()
        else:
            err = "Book not found!"
            messages.error(request, err)
    return redirect('manage_return_requests')

@user_passes_test(is_admin)
def approve_request(request, rqid):
    user_req = Request.objects.get(pk=rqid)
    if not user_req.is_approved:
        user_req.is_approved = True
        book = Book.objects.get(book_code=user_req.request_book_code)
        book.issued_to = user_req.request_user
        book.returned_date = user_req.return_date
        book.issued_date = timezone.now()
        book.is_available = False
        book.save()
        user_req.save()
        msg = "Request Approved! Book issued to {}".format(user_req.request_user)
        messages.success(request, msg)
        user_req.delete()
    return redirect('manage_requests')


# def upload_image(image_path, book_code):
#     with open(image_path, 'rb') as f:
#         call_command(
#             'shell',
#             '--command', 
#             f'''
#             from library.models import Book; 
#             Book.objects.filter(book_code={book_code}).update(image_field=File(f))'
#             '''
#         )
# 

@user_passes_test(is_admin)
def user_books_admin_view(request, user):
    return render(request, 'libadmin/user_books_admin_view.html', {'userbooks':  Book.objects.filter(issued_to=user)})


@user_passes_test(is_admin)
def manage_penalties(request):
    import datetime
    today = datetime.datetime.today()

    books = Book.objects.all()
    penalities = []
    unavlbl_books = [book for book in books if not book.is_available]
    for book in unavlbl_books:
        if book.returned_date:
          rd = datetime.datetime(
              book.returned_date.year, 
              book.returned_date.month, 
              book.returned_date.day, 
          )
          if rd < today:
              penalities.append(book)
    return render(request, 'libadmin/manage_penalties.html', {'books': penalities})