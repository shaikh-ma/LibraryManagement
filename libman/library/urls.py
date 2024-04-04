from django.urls import path
from .views import BookListView, UserBooksListView, new_request, UserRequestsListView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path('user/<str:username>', UserBooksListView.as_view(), name='user-books'),
    path('requests/new_request', new_request, name='new-user-requests'),
    path('requests/<str:username>', UserRequestsListView.as_view(), name='user-requests'),
]