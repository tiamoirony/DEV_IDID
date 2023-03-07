from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

# Create your views here.

from .models import Todo
from .forms import TodoForm


def todo_list(request):

    # todo 전체 목록 추출 후 전송
    # select title, created from todo where complete = 0

    todos = Todo.objects.filter(complete=False)

    return render(
        request, "todo/todo_list.html", {"todos": todos}
    )  # 키 벨류 형태로 전송하기 render


def todo_detail(request, pk):

    # pk 에 해당하는 todo 가져오기 + 전송

    todo = get_object_or_404(Todo, id=pk)

    return render(request, "todo/todo_detail.html", {"todo": todo})


def todo_register(request):

    # get/post
    # get TodoForm 번 상태로
    # post TodoForm에 사용자의 입력값을 담은 상태로

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()

            return redirect("todo_detail", pk=todo.id)

    else:
        form = TodoForm()

    return render(request, "todo/todo_create.html", {"form": form})


def todo_edit(request, pk):

    # get pk에 해당하는 내용 가져와서 보내주기
    # post 수정 내용 가져와서 저장
    # update todo set important = 1 where

    todo = get_object_or_404(Todo, id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("todo_list")

    else:
        form = TodoForm(instance=todo)

    return render(request, "todo/todo_edit.html", {"form": form})


def todo_done(request, pk):

    todo = get_object_or_404(Todo, id=pk)
    todo.complete = True
    todo.save()

    return redirect("todo_list")


def done_list(request):
    # complete 가 true인 todo 추출

    dones = Todo.objects.filter(complete=True)

    return render(request, "todo/done_list.html", {"dones": dones})
