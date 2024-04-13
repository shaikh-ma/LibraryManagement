from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def library_admin(request):
    return render(request, 'libadmin/admin.html')


@user_passes_test(is_admin)
def manage_books(request):
    return render(request, 'libadmin/manage_books.html')


@user_passes_test(is_admin)
def manage_users(request):
    return render(request, 'libadmin/manage_users.html')


@user_passes_test(is_admin)
def manage_requests(request):
    return render(request, 'libadmin/manage_requests.html')

