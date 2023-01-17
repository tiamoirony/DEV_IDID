from django.shortcuts import render

from .form import RegisterForm

# Create your views here.


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():  # 검증하기
            form.save()
    else:
        form = RegisterForm()

    return render(request, "users/register.html", {"form": form})
