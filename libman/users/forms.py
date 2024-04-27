from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

CHOICE_YEAR =(
("1", "First Year"),
("2", "Second Year"),
("3", "Third Year"),
("4", "Other"),
)

class UserRegisterForm(UserCreationForm):
    roll_no = forms.IntegerField()
    icard_no = forms.IntegerField()
    # mobile_number = forms.IntegerField()
    class_div = forms.ChoiceField(choices=CHOICE_YEAR)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', 
            'roll_no',
            'icard_no',
            'class_div',
            'email', 
            # 'mobile_number',
            'password1', 
            'password2'
            ]


class UserPasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['password']

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Password is required.")
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return password
    