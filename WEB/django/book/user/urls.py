
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views


# app_name = 'users'

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    

]



    # # custom login / logout 구현
    # # path("login/", views.islogin, name='login'),
    # # path("logout/", views.common_logout, name='logout'),
    
    
    # #djan django.contrib.auth.urls
    # path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    # path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    
    # # path("password_change/", auth_views.PasswordChangeView.as_view(), name='password_change'),
    # # path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    
    # # path("password_change/", views.CustomPasswordChangeView.as_view(), name='password_change'),