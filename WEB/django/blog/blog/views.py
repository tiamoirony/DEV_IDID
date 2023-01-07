from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Post
from .forms import PostForm

def post_list(request):
    
    '''글목록 추출 
    
    '''
    posts = Post.objects.order_by('-created_at')
        
    return render(request, "blog/post_list.html", {'posts':posts})

@login_required(login_url='login')
def post_write(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid(): # 검증하기
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            
            return redirect('post_list')
        
    else:
        form = PostForm()
        
        
    return render(request,'blog/post_write.html',{'form':form})

def post_detail(request, pk):
    
    post = get_object_or_404(Post, pk=pk) # 조회
    
    # form = PostForm(instance=post) # form 담기
    
    
    return render(request,'blog/post_detail.html',{'post':post})