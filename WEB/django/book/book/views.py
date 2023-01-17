from django.shortcuts import render, redirect, get_object_or_404
from .form import BookForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .models import Book
from django import forms

# 전체 목록 추출
def list(request):

    book_list = Book.objects.all()

    return render(request, "book/book_list.html", {"book_list": book_list})


def detail(request, pk):

    detail = get_object_or_404(Book, pk=pk)

    return render(request, "book/book_detail.html", {"detail": detail})


def update(request, pk):

    book = get_object_or_404(Book, pk=pk)

    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return redirect("detail", pk=book.pk)

    else:
        form = BookForm(instance=book)

    return render(request, "book/book_update.html", {"form": form})


def remove(request, pk):

    book = get_object_or_404(Book, pk=pk)
    book.delete()

    return redirect("list")


def create(request):

    if request.method == "POST":

        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")

    else:
        form = BookForm()

    return render(request, "book/book_create.html", {"form": form})


# Create your views here.

# def signup(request):

#     if request.method == 'POST':
#         # post로 넘어오는 모든 입력값을 form과 연결
#         form = UserForm(request.POST)
#         if form.is_valid(): # 검증하기
#             form.save()
#             return redirect('users:login')

#     else:
#         form = UserForm()


#     return render(request,'users/register.html',{'form':form})


# def islogin(request):

#     if request.method == 'POST':
#         #username, password 가져오기
#         username = request.POST['username']
#         password = request.POST['password']

#         user = authenticate(request, username=username, password=password)

#         # db 확인

#         # 세션
#         if user is not None:
#             login(request, user)
#             return redirect('index')

#     return render(request,'users/login.html')

# def common_logout(request):
#     # 세션 해제
#     logout(request)
#     return redirect('index')

# class CustomPasswordChangeView(PasswordChangeView):

# 사용자가 바뀐 비밀번호로 재 로그인을 하지 않아도 됨
# update_session_auth_hash(self.request, form.user)

# success_url = reverse_lazy("users:login")
# template_name = "users/password_change.html"
