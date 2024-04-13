from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.library_admin, name='library_admin'),
]