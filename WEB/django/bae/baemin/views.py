from django.shortcuts import render, get_object_or_404, redirect
from .models import Shop
from .form import OrderForm

from django.contrib.auth.decorators import login_required

# Create your views here.



def index(request):
    return render(request, 'baemin/index.html', {
        'shop_list':Shop.objects.all(),
    })
    
@login_required
def order_new(request, pk):
    shop = get_object_or_404(Shop, id=pk)
    if request.method == 'POST':
        form = OrderForm(shop, request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.shop = shop
            order.save()
            form.save_m2m()
            return redirect('profile')
        pass
    else:
        form = OrderForm(shop)
    return render(request, 'baemin/order_form.html',{
        'form':form,
        'shop':shop
    })