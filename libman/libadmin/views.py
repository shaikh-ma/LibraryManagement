from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from library.models import Book, Request, User
from django.contrib import messages
from django.utils import timezone


def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def library_admin(request):
    return render(request, 'libadmin/admin.html')


# @user_passes_test(is_admin)
# def manage_books(request):
#     books = Book.objects.all()
#     return render(request, 'libadmin/manage_books.html', {'books': books})

@user_passes_test(is_admin)
def manage_requests(request):
    requests = Request.objects.all()
    return render(request, 'libadmin/manage_requests.html', {'requests': requests})


@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'libadmin/manage_users.html', {'users': users})


@user_passes_test(is_admin)
def delete_book(request, bookid):
    book = Book.objects.get(pk=bookid)
    if book:
        book.delete()
        msg = "Delete book - {}!".format(book.title)
        messages.success(request, msg)
    return redirect('home')

@user_passes_test(is_admin)
def approve_request(request, rqid):
    user_req = Request.objects.get(pk=rqid)
    if not user_req.is_approved:
        user_req.is_approved = True
        book = Book.objects.get(pk=user_req.request_book_id)
        book.issued_to = user_req.request_user
        book.returned_date = user_req.return_date
        book.issued_date = timezone.now()
        book.is_available = False
        book.save()
        user_req.save()
        msg = "Request Approved! Book issued to {}".format(user_req.request_user)
        messages.success(request, msg)
        user_req.delete()
    return redirect('home')


# @user_passes_test(is_admin)
# def edit_book(request, bookid):
#     book = Book.objects.get(pk=bookid)
#     if book:
#         book.delete()
#         msg = "Delete book - {}!".format(book.title)
#         messages.success(request, msg)
#     return redirect('home')
