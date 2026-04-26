from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Profile


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


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')
        labels = {
            'username': 'Имя пользователя',
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = (
            'bio',
            'birth_date',
            'height_cm',
            'weight_kg',
            'daily_calorie_goal',
            'show_diary_to_friends',
        )
        labels = {
            'bio': 'О себе',
            'birth_date': 'Дата рождения',
            'height_cm': 'Рост (см)',
            'weight_kg': 'Вес (кг)',
            'daily_calorie_goal': 'Дневная норма калорий',
            'show_diary_to_friends': 'Показывать мой дневник другим пользователям',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
