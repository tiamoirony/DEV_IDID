from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question

from ..forms import QuestionForm

# Create your views here.

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def question_update(request, question_id):
    """
    질문 수정 - form 사용 
    """
    question = get_object_or_404(Question, id=question_id)

    if request.method == "POST":

        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)  # 작성자 나오게 함
            question.author = request.user
            question.save()
            return redirect("detail", question_id=question_id)

    else:
        form = QuestionForm(instance=question)

    return render(request, "board/question_update.html", {"form": form})


@login_required(login_url="login")  # 로그인 하면 되는 작업
def question_delete(request, question_id):

    question = get_object_or_404(Question, id=question_id)
    if request.user != question.author:

        return redirect("detail", question_id=question_id)

    question.delete()

    return redirect("index")


@login_required(login_url="login")
def question_create(request):

    if request.method == "POST":

        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)  # 작성자 나오게 함
            question.author = request.user
            question.save()
            return redirect("index")

    else:
        form = QuestionForm()
    pass

    return render(request, "board/question_form.html", {"form": form})
