
from django.urls import path
from django.views.generic.base import TemplateView
from . import views

from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.board_list , name='board_list'),
    path("create/", views.board_write , name='board_write'),
    path("<int:pk>", views.board_detail , name='board_detail'),
]




    