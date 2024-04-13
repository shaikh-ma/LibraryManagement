from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from library.models import Book, Request, User

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
def manage_users(request):
    users = User.objects.all()
    return render(request, 'libadmin/manage_users.html', {'users': users})

