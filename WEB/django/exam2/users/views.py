from django.shortcuts import render, redirect
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy


# Create your views here.


def signup(request):

    if request.method == "POST":
        # post로 넘어오는 모든 입력값을 form과 연결
        form = UserForm(request.POST)
        if form.is_valid():  # 검증하기
            form.save()
            return redirect("users:login")

    else:
        form = UserForm()

    return render(request, "users/register.html", {"form": form})


def islogin(request):

    if request.method == "POST":
        # username, password 가져오기
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        # db 확인

        # 세션
        if user is not None:
            login(request, user)
            return redirect("index")

    return render(request, "users/login.html")


def common_logout(request):
    # 세션 해제
    logout(request)
    return redirect("index")


class CustomPasswordChangeView(PasswordChangeView):

    # 사용자가 바뀐 비밀번호로 재 로그인을 하지 않아도 됨
    # update_session_auth_hash(self.request, form.user)

    success_url = reverse_lazy("users:login")
    template_name = "users/password_change.html"
