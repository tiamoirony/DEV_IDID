from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question, Answer

from ..forms import AnswerForm

# Create your views here.

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def answer_create(request, question_id):

    if request.method == "POST":

        question = get_object_or_404(Question, pk=question_id)

        form = AnswerForm(request.POST)
        if form.is_valid():

            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            return redirect("detail", question_id=question_id)

    else:
        form = AnswerForm()

    return render(
        request, "board/question_detail.html", {"form": form, "question": question}
    )  # 내용도 가져오기


@login_required(login_url="login")
def answer_update(request, answer_id):

    answer = get_object_or_404(Answer, id=answer_id)

    if request.method == "POST":

        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            question = form.save(commit=False)  # 작성자 나오게 함
            question.author = request.user
            question.save()
            return redirect("detail", question_id=answer.question_id)

    else:
        form = AnswerForm(instance=answer)

    return render(request, "board/answer_form.html", {"form": form})


@login_required(login_url="login")
def answer_delete(request, answer_id):

    answer = get_object_or_404(Answer, id=answer_id)
    if request.user != answer.author:

        return redirect("detail", question_id=answer.question_id)

    answer.delete()

    return redirect("index")
