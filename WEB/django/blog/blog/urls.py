from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("write/", views.post_write, name="post_write"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("comment/create/", views.comment_create, name="comment_create"),
    path("post/like/", views.post_like, name="post_like"),
]
