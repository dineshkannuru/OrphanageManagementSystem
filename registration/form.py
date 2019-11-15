from django import forms
from django.db import models
from registration import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder': 'Password'}))

    # def clean(self):
    #     username = self.cleaned_data.get('username')
    #     if models.User.objects.filter(username=username).exists():
    #
    #         self.add_error(None, "Hey, Please enter a correct username and password. Note that both fields may be case-sensitive.")


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), validators=[MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

    class Meta:
        model = models.User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password']
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'first_name' : forms.TextInput(attrs={'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last name'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'E-mail'})
        }

    def clean(self):
        cleaned_data = super().clean()

        username = cleaned_data.get("username")
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if models.User.objects.filter(username=username).exists():
            self.add_error("username", "This username already exists. Please choose another")

        if models.User.objects.filter(email=email).exists():
            self.add_error("email", "A user with this email already exists. Please login to your account")

        if password != confirm_password:
            self.add_error("confirm_password", "Both the Passwords Do Not Match!")
