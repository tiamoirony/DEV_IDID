from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
from .models import Item
from .forms import ItemForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):

    return render(request, "order/index.html")


def cart(request):
    return render(request, "order/cart.html")


def order_new(request):

    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # 작성자 나오게 함

            return redirect("cart")
    else:
        form = ItemForm()

    return render(request, "order/index.html", {"form": form})
