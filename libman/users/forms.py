from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

CHOICE_TYPE =(
("1", "Student"),
("2", "Professor"),
("3", "Library Staff"),
("4", "Other"),
)

def validate_mobile_number(mob_number):
    if not mob_number.isdigit():
        raise ValidationError("Invalid mobile number")
    
def validate_existing_user(email):
    if User.objects.filter(email=email):
        raise ValidationError("User with this emails address already exists.")

                        
class UserRegisterForm(UserCreationForm):
    firstname  = forms.CharField(max_length=200)
    lastname  = forms.CharField(max_length=200)
    email = forms.EmailField(validators=[validate_existing_user])
    mobile_number = forms.CharField(max_length=10, min_length=10, validators=[validate_mobile_number])
    user_type = forms.ChoiceField(choices=CHOICE_TYPE)
    icard_no = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'firstname',
            'lastname',
            'username', 
            'email', 
            'mobile_number',
            'password1', 
            'password2',
            'icard_no',
            'user_type',
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
    