from django.urls import path
from . import views
from libadmin import views as adviews
from users import views as usviews

urlpatterns = [
    path("", views.BookListView.as_view(), name="home"),
    path("about", views.about_page, name="about"),
    path('user/<str:username>', views.UserBooksListView.as_view(), name='user-books'),
    path('new_request/', views.new_request, name='new-user-request'),
    path('return_request/<int:bookid>', views.request_book_return, name='request-return'),
    path('requests/<str:username>', views.UserRequestsListView.as_view(), name='user-requests'),
    path('requests/return/<str:username>', views.UserReturnRequestsListView.as_view(), name='user-return-requests'),
    path('requests/<str:username>/<int:pk>', views.RequestDetailView.as_view(), name='request_detail'),
    path("book/<int:pk>/", views.BookDetailView.as_view(), name="book_detail"),
    path("admin", adviews.library_admin, name="admin_login"),
    path('admin/manage_books', adviews.manage_books, name='manage_books'),
    path('admin/manage_requests', adviews.manage_requests, name='manage_requests'),
    path('admin/manage_return_requests', adviews.manage_return_requests, name='manage_return_requests'),
    path('admin/manage_users', adviews.manage_users, name='manage_users'),
    path('admin/manage_penalties', adviews.manage_penalties, name='manage_penalties'),
    path('admin/book/<int:bookid>/delete', adviews.delete_book, name='delete_book'),
    path('admin/requests/<int:rqid>/approve', adviews.approve_request, name='approve_request'),
    path('admin/requests/<int:rqid>/delete', adviews.delete_request, name='delete_request'),
    path('admin/users/<int:rqid>/delete', adviews.delete_user, name='delete_user'),
    path('admin/book/add', adviews.add_new_book, name='add_new_book'),
    path('admin/book/edit/<int:bookid>', adviews.edit_book, name='edit_book'),
    path('return/<int:pk>', adviews.ReturnRequest, name='approve_book_return'),
    path('admin/return/requests/<int:rqid>/confirm', adviews.confirm_return, name='confirm_return'),
    path('user_books_admin/<str:user>/', adviews.user_books_admin_view, name='user-books-admin-view'),
    path("profile/<str:username>/", usviews.ProfileDetailView.as_view(), name="profile"),
]