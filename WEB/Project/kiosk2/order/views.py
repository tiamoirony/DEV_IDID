from django.shortcuts import render, redirect,get_object_or_404


# Create your views here.
from .models import Item
from .forms import OrderForm

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    
    return render(request, 'order/index.html')


def cart(request):
    return render(request,'order/cart.html')


@login_required
def order_new(request):
    pass    

    # shop = get_object_or_404(Shop)
    # if request.method == 'POST':
    #     form = OrderForm(shop, request.POST)
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.user = request.user
    #         order.shop = shop
    #         order.save()
    #         form.save_m2m()
    #         return redirect('cart')
    # else:
    #     form = OrderForm()
    # return render(request, 'order/index.html',{
    #     'form':form,
    #     'shop':shop
    # })