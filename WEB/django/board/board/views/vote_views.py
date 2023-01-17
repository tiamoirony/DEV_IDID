from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question, Answer, Comment


# Create your views here.

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
from django.contrib import messages


@login_required(login_url="login")
def vote_question(request, question_id):

    question = get_object_or_404(Question, id=question_id)

    # 로그인 사용자가 현재 게시물에 좋아요 누른 정보가 있는지 확인
    if question.author != request.user:
        question.voter.add(request.user)

    else:
        messages.error(request, "본인 추천 안됨")

    return redirect("detail", question_id=question_id)


@login_required(login_url="login")
def vote_answer(request, answer_id):

    answer = get_object_or_404(Answer, id=answer_id)

    if answer.author != request.user:
        answer.voter.add(request.user)

    else:
        messages.error(request, "본인 추천 안됨ff")

    return redirect("detail", question_id=answer.question.id)

