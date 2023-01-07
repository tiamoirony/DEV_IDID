from django.shortcuts import render,redirect
from .forms import UserForm
# Create your views here.


def register(request):
    
    if request.method == 'POST':
        
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

        
    else:
        form = UserForm()
    
    return render(request,'user/register.html',{'form':form})

