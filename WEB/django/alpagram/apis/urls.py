from django.urls import path
from . import views

urlpatterns = [   

    # http://127.0.0.1:8000/apis/
    
    # 회원가입
    # users/create/  name=user_create
    path("users/create/", views.UserCreateView.as_view(), name="user_create"),
]


