from django.urls import path, include, reverse_lazy
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="user/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("register/", views.register, name="register"),
    path(
        "password_change/",
        auth_views.PasswordChangeView.as_view(
            template_name="user/password_change.html",
            success_url=reverse_lazy("password_change_done"),
        ),
        name="password_change",
    ),
    # path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
    # path("", include('django.contrib.auth.urls')),
    path(
        "password_reset/", views.UserPasswordResetView.as_view(), name="password_reset"
    ),
    path(
        "password_reset/done/",
        views.UserPasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        views.UserPasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path(
        "reset/done/",
        views.UserPasswordResetConpleteView.as_view(),
        name="password_reset_complete",
    ),
]
