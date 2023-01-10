from django.shortcuts import render, redirect, get_object_or_404
from .models import Board
from .forms import BoardForm

from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

def board_list(request):

    all_boards = Board.objects.order_by('-register_dttm')
    
    # 사용ㅈ가ㅏ 요청한 페이지 번호
    page = request.GET.get('page',1)
    
    # 객체를 이요한 보야줄 페이지 결정 
    paginator = Paginator(all_boards, 10)
    
    boards = paginator.get_page(page)
    
    return render(request, 'board/board_list.html',{'boards':boards})


@login_required(login_url='login')
def board_write(request):
    
    if request.method =='POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer = request.user
            board.save()
            
            # 태그 저장 따로 
            form.save_m2m()
            
            return redirect('board_list')
    else:
        form = BoardForm()
    
    
    return render(request, 'board/board_create.html',{'form':form})


def board_detail(request, pk):
    
    board = get_object_or_404(Board, pk=pk) # Board.objects.get(id=1)

    return render(request, 'board/board_detail.html', {'board':board})
