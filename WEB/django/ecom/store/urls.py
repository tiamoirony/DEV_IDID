from django.urls import path, include
from . import views

from store.controller import authview, cart


urlpatterns = [
    path("home/", views.home, name="home"),
    path("collections/", views.collections, name="collections"),
    path("collections/<str:slug>", views.collectionsview, name="collectionsview"),
    path(
        "collections/<str:cate_slug>/<str:prod_slug>",
        views.productview,
        name="productview",
    ),
    # 카테고리 슬러그, 프로덕션 슬러그
    path("register/", authview.register, name="register"),
    path("login/", authview.loginpage, name="loginpage"),
    path("logout/", authview.logoutpage, name="logoutpage"),
    path("add-to-cart", cart.addtocart, name="addtocart"),
    path("cart", cart.viewcart, name="cart"),
    path("update-cart", cart.updatecart, name="updatecart"),
    path("delete-cart-item", cart.deletecartitem, name="deletecartitem"),
]
