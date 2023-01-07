
from django.urls import path, include

from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    
    path('', views.index, name='index'),
    path('<int:pk>/new/', views.order_new, name='order_new'),
    
]

