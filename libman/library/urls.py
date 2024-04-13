from django.urls import path
from . import views
from libadmin import views as adviews

urlpatterns = [
    path("", views.BookListView.as_view(), name="home"),
    path('user/<str:username>', views.UserBooksListView.as_view(), name='user-books'),
    path('new_request/', views.new_request, name='new-user-request'),
    path('requests/<str:username>', views.UserRequestsListView.as_view(), name='user-requests'),
    path('requests/<str:username>/<int:pk>', views.RequestDetailView.as_view(), name='request_detail'),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("admin", adviews.library_admin, name="admin_login"),
    path('admin/manage_books', adviews.manage_books, name='manage_books'),
    path('admin/manage_requests', adviews.manage_requests, name='manage_requests'),
    path('admin/manage_users', adviews.manage_users, name='manage_users'),
]