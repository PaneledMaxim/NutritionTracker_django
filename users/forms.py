from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Имя', max_length=150, required=False)
    last_name = forms.CharField(label='Фамилия', max_length=150, required=False)

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя')
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
