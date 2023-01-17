"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from board.views import base_views

from django.urls import reverse_lazy

urlpatterns = [
    
    
    path("admin/", admin.site.urls),
    path("board/", include("board.urls")),
    path("user/", include("user.urls")),
    path("", base_views.index),
    
    
    
    
    # 회원가입 시 입력했던 이메일을 입력할 수 있는 화면 제공 
    # path("", include('django.contrib.auth.urls')),
    
    # path("password_reset/", auth_views.PasswordResetView.as_view(), name='password_reset'),
    # # 새 비밀번호가 전송 되었습니다. 화면 (회원이 있는지 확인, 이메일 전송 )
    # path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # # 전송된 이메일 내용에 비밀번호를 새롭게 변경 할수 있는 링크 제공 
    # path("reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # # 비밀번호가 변경 되었습니다. 화면 ((로그인 링크 제공 ))
    # path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    # 클래스 뷰 

    
]

