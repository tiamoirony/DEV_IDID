from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
)

# Create your views here.

from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy


def register(request):

    """
    회원가입
    """
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():  # 검증하기
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
            return redirect("index")

    else:
        form = UserForm()

    return render(request, "user/register.html", {"form": form})


class UserPasswordResetView(PasswordResetView):
    # 이메일을 입력할 수 있는 화면
    template_name = "user/password_reset_form.html"
    # 이메일이 존재하는 경우 그 다음 작업을 진행할 경로 지정
    success_url = reverse_lazy("password_reset_done")
    # 이메일로 전송될 페이지 지정
    email_template_name = "user/password_reset_email.txt"

    def form_valid(self, form):
        # 사용자가 입력한 이메일이 실제 존재하는지 확인 후 없으면 에러 메세지 전송
        # 존재 한다면 유효성 검증

        if User.objects.filter(email=self.request.POST.get("email")).exists():
            return super().form_valid(form)
        else:
            messages.info(self.request, "이메일을 확인해 주세요 ")
            return redirect("password_reset")


class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = "user/password_reset_done.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "user/password_reset_confirm.html"


class UserPasswordResetConpleteView(PasswordResetCompleteView):
    template_name = "user/passwrd_reset_complete.html"
