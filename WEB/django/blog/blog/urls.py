from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("write/", views.post_write, name="post_write"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]
