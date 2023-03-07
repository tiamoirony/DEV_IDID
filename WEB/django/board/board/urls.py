from django.urls import path, include
from .views import answer_views, base_views, question_views, comment_views, vote_views

urlpatterns = [
    path("", base_views.index, name="index"),
    path("<int:question_id>/", base_views.detail, name="detail"),
    path(
        "answer/create/<int:question_id>/",
        answer_views.answer_create,
        name="answer_create",
    ),
    path(
        "answer/update/<int:answer_id>/",
        answer_views.answer_update,
        name="answer_update",
    ),
    path(
        "answer/delete/<int:answer_id>/",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    path("answer/vote/<int:answer_id>/", vote_views.vote_answer, name="vote_answer"),
    path("question/create/", question_views.question_create, name="question_create"),
    path(
        "question/update/<int:question_id>/",
        question_views.question_update,
        name="question_update",
    ),
    path(
        "question/delete/<int:question_id>/",
        question_views.question_delete,
        name="question_delete",
    ),
    path(
        "question/vote/<int:question_id>/",
        vote_views.vote_question,
        name="vote_question",
    ),
    ### comment
    path(
        "comment/create/question/<int:question_id>",
        comment_views.comment_question_create,
        name="comment_question_create",
    ),
    path(
        "comment/update/question/<int:comment_id>",
        comment_views.comment_question_update,
        name="comment_question_update",
    ),
    path(
        "comment/delete/question/<int:comment_id>",
        comment_views.comment_question_delete,
        name="comment_question_delete",
    ),
    path(
        "comment/create/answer/<int:answer_id>",
        comment_views.comment_answer_create,
        name="comment_answer_create",
    ),
    path(
        "comment/update/answer/<int:comment_id>",
        comment_views.comment_answer_update,
        name="comment_answer_update",
    ),
    path(
        "comment/delete/answer/<int:comment_id>",
        comment_views.comment_answer_delete,
        name="comment_answer_delete",
    ),
]
