
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.order_new, name='order_new'),
    
    path('cart/', views.cart, name='cart'),
]