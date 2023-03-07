from django.urls import path
from . import views

urlpatterns = [
    # 회원가입
    path("users/create/", views.UserCreateView.as_view(), name="userCreate"),
    path(
        "users/profile/update/",
        views.UserProfileImageDelete.as_view(),
        name="user_profile_delete",
    ),
    path(
        "users/profile/update/",
        views.UserProfileImageUpdate.as_view(),
        name="user_profile_update",
    ),
    path("contents/create/", views.ContentCreateView.as_view(), name="contents_create"),
]
