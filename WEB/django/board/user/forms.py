from django.contrib.auth.models import User
from django import forms

# UserForm 생성

from django.contrib.auth.forms import UserCreationForm


class UserForm(UserCreationForm):

    email = forms.EmailField(label="이메일")

    class Meta:
        model = User
        fields = ["username", "email"]
