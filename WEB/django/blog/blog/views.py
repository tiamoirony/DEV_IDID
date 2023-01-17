from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm

from django.contrib import messages

from django.http import JsonResponse


def post_list(request):

    """글목록 추출 
    
    """
    posts = Post.objects.order_by("-created_at")

    return render(request, "blog/post_list.html", {"posts": posts})


@login_required(login_url="login")
def post_write(request):

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():  # 검증하기
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            # 태그만 따로 저장 manytomany 필드 저장
            form.save_m2m()

            return redirect("post_list")

    else:
        form = PostForm()

    return render(request, "blog/post_write.html", {"form": form})


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)  # 조회

    # 좋아요
    is_liked = False

    # form = PostForm(instance=post) # form 담기
    # 조회한 post에 로그인 유저가 좋아요 를ㄹ 눌렀는지 여부

    if post.likes.filter(id=request.user.id).exists():
        is_liked = True

    return render(
        request, "blog/post_detail.html", {"post": post, "is_liked": is_liked}
    )


@login_required(login_url="login")
def comment_create(request):

    if request.method == "POST":
        content = request.POST["content"]
        post_id = request.POST.get("post_id", "").strip()

        if content and post_id:
            # 삽입 user 로그인 사용자, post 원본글 , content 댓글
            comment = Comment.objects.create(
                user=request.user, post_id=post_id, content=content
            )
            # post_detail 돌아가기
            return redirect("post_detail", post_id)
            # return redirect('post_detail', pk=post_id)

    messages.error(request, "댓글을 입력해 주세요 ")
    return redirect("post_detail", pk=post_id)


def post_like(request):

    # 비동기식 좋아요 클릭

    # 글 번호에 해당하는 게시물 찾기
    post_id = request.POST["id"]

    post = get_object_or_404(Post, id=post_id)

    # 로그인 사용자가 현재 게시물에 좋아요 누른 정보가 있는지 확인

    is_liked = post.likes.filter(id=request.user.id).exists()

    if is_liked:
        post.likes.remove(request.user)
        is_liked = False

    else:
        post.likes.add(request.user)
        is_liked = True

    return JsonResponse({"likes": post.likes.count(), "is_liked": is_liked})
