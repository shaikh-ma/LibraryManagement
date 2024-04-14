from django import forms
from .models import Request, Book, ReturnRequest


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = (
            'request_book',
            'return_date')
        exclude = ("request_user",)

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
           "title",
           "author",
           "book_code",
           "summary",
           "image",
        )

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
           "title",
           "author",
           "book_code",
           "summary",
           "image",
        )

class ReturnRequestForm(forms.ModelForm):
    class Meta:
        model = ReturnRequest
        fields = ()
        exclude = ["request_user",]