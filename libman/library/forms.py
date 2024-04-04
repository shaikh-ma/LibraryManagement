from django import forms


class RequestForm(forms.Form):
    book_title = forms.CharField(label="Book Title")
    user_id = forms.CharField(label="User ID")