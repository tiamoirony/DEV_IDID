# form 을 생성
# 일반 폼, 모델 폼 상속
#UserForm 생성  ==> User 모델 
# UserCreationForm : User모델 + form 가능


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email']