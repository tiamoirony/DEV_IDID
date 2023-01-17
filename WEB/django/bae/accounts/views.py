from django.shortcuts import render, redirect
from .form import UserForm

# Create your views here.


def signup(request):
    # 회원가입
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # 검증하기
            form.save()
            return redirect("login")

    else:
        form = UserForm()

    return render(request, "accounts/signup.html", {"form": form})


def profile(request):
    return render(request, "accounts/profile.html")
