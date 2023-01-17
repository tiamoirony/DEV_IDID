from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/", views.sign_up, name="signup"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LoginView.as_view(), name="logout"),
]
