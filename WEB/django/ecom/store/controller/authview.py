from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from store.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == 'POST':
        form =CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            # 회원가입 완료 후 바로  로그인 처리도 해주고 싶다

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(
                request, username=username, password=password
            )  # db에서 가져오기

        # 세션에 정보 저장
        if user is not None:
            login(request, user)
            return redirect("home")
        
    context = {'form':form}
    return render(request, 'auth/register.html', context)


def loginpage(request):
    
    if request.user.is_authenticated:
        messages.warning(request, 'You are already logged in')
        return redirect('home')
    else:
        if request.method =='POST':
            name = request.POST.get('username')
            passwd = request.POST.get('password')

            user = authenticate(request, username=name, password=passwd)
            
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in Successfully')
                return redirect("home")
            else:
                messages.error(request, 'Invalid Username or Password')
                return redirect('login')
    
        return render(request, 'auth/login.html')


def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out Successfully')
    return redirect("home")