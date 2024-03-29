from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from home.models import User



class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=100, help_text="Must be unique")
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(), label="Password")
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(), label="Repeat password")
    photo = forms.ImageField(help_text="Not required", required=False)
    background = forms.ImageField(help_text="Not required", required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'photo', 'background')