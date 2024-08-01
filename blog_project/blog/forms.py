# blog/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Post, Comment  # Используйте относительный импорт для моделей

class SimpleUserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), help_text='Введите пароль.')
    password_confirm = forms.CharField(widget=forms.PasswordInput(), help_text='Подтвердите пароль.')

    class Meta:
        model = User
        fields = ['username']

    def clean_password_confirm(self):
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают")
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
