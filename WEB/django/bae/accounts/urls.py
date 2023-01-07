
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path("register/", views.register, name='register'),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login', kwargs={
        'next_page': 'accounts/profile.html'}),
    path("signup/", views.signup, name='signup'),
    path("logout/", auth_views.LogoutView.as_view(), name='logout'),
    path("profile/", views.profile, name='profile'),
]

