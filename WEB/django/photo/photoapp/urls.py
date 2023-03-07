"""config URL Configuration


Examples:
Function views
    1. Add an import:  from my_ap  2. Add a URL to urlpatterns:  path('', views.home, name='home')

"""
from . import views

from django.urls import path

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", views.home, name="home"),
    # http://127.0.0.1:8000/photo/new + get post
    path("new/", views.post, name="post"),
    # http://127.0.0.1:8000/photo/2
    path("<int:pk>/", views.detail, name="detail"),
    # http://127.0.0.1:8000/photo/2/remove
    path("<int:pk>/remove/", views.remove, name="remove"),
    # http://127.0.0.1:8000/photo/2/edit
    path("<int:pk>/edit/", views.edit, name="edit"),
]
