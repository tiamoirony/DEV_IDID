from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question, Answer, Comment

from ..forms import CommentForm

# Create your views here.

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def comment_question_create(request, question_id):
    """
    comment
    """
    pass
    if request.method == "POST":

        question = get_object_or_404(Question, pk=question_id)

        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)  # (commit=False) 임시저장
            comment.author = request.user
            comment.question = question
            comment.save()
            return redirect("detail", question_id=question_id)

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="login")
def comment_question_update(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)  # 작성자 나오게 함
            comment.save()
            return redirect("detail", question_id=comment.question.id)

    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="login")
def comment_question_delete(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    comment.delete()

    return redirect(
        "detail", question_id=comment.question.id
    )  # comment.question_id 질문번호의 코멘트번호를 질문번호로 넘긴다


@login_required(login_url="login")
def comment_answer_create(request, answer_id):
    """
    comment
    """
    pass
    if request.method == "POST":

        answer = get_object_or_404(Answer, pk=answer_id)

        form = CommentForm(request.POST)
        if form.is_valid():

            comment = form.save(commit=False)  # (commit=False) 임시저장
            comment.author = request.user
            comment.answer = answer
            comment.save()
            return redirect("detail", question_id=answer.question.id)

    else:
        form = CommentForm()

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="login")
def comment_answer_update(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    if request.method == "POST":

        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)  # 작성자 나오게 함
            comment.save()
            return redirect("detail", question_id=comment.answer.question.id)

    else:
        form = CommentForm(instance=comment)

    return render(request, "board/comment_form.html", {"form": form})


@login_required(login_url="login")
def comment_answer_delete(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)

    comment.delete()

    return redirect(
        "detail", question_id=comment.answer.question.id
    )  # comment.question_id 질문번호의 코멘트번호를 질문번호로 넘긴다
