from django.urls import path
from .views import BookListView, UserBooksListView

urlpatterns = [
    path("", BookListView.as_view(), name="home"),
    path('user/<str:username>', UserBooksListView.as_view(), name='user-books'),
]