# 장고 User 대체 
# 속성  username, password, email, firtst_name, last_name


# from django.contrib.auth.models import User
# user = User.objects.create_user('join', 'join@gmail.com', 'joinpassword')
# user.save()


# 사용자 인증
# select count(*) from user where username='join' and password = 'johnpassword'
# count가 1이라면 승인 

# from django.contrib.auth import authenticate, login

# user = authenticate(request, username)

# login(request,user)


#authenticate

# # 비밀번호 변경 
# u = User.objects.get(username='join')
# u.set_password('123')
# u.save


# 모델폼 상속, 모델 폼 상속 

# 장고 꺼 
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserForm(UserCreationForm):
    
    # 상속시 이메일은 필수 상속 항목이 아니라 설정 필요 
    email = forms.EmailField(label='이메일')
    
    class Meta:
        model = User
        fields = ['username','email']
        


