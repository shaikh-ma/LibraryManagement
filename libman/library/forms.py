from django import forms
from .models import Request


class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = (
            'request_user', 
            'request_book',
            'request_book_title',
            'request_book_code',
            'return_date')