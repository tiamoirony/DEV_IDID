from django.shortcuts import render, redirect, get_object_or_404
from ..models import Question, QuestionCount
from django.db.models import Q, Count
# Create your views here.

from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from common.utils import get_client_ip


def index(request):
    
    

    page = request.GET.get("page", 1)
    
    keyword = request.GET.get("keyword","" )
    
    so = request.GET.get('so','')



    if so =='recommend':
        question_list = Question.objects.annotate(num_voter = Count('voter')).order_by('-num_voter','-created_at' )
    elif so == 'popular':
        question_list = Question.objects.annotate(num_answer = Count('answer')).order_by('-num_answer','-created_at' )
    else:
        question_list = Question.objects
    
    
    
    question_list = Question.objects.order_by("-created_at")


    if keyword:
        question_list = question_list.filter(
            Q(subject__icontains=keyword) |
            Q(content__icontains=keyword) |
            Q(author__username__icontains=keyword)|
            Q(answer__author__username__icontanins=keyword)).distinct()

    
    paginator = Paginator(question_list, 10)
    page_obj = paginator.get_page(page)

    return render(request, "board/question_list.html", {"question_list": page_obj, "page":page, "keyword":keyword, "so":so})






def detail(request, question_id):

    
    
    page = request.GET.get("page", 1)
    
    keyword = request.GET.get("keyword","" )
    
    so = request.GET.get('so','recent')
    
    question =  get_object_or_404(Question, id=question_id)
    
    
    ip = get_client_ip(request)
    #  현재 질문의 조회수 찾기 

    cnt = QuestionCount.objects.filter(ip=ip, question=question).count()
    
    if cnt == 0:
        qc =QuestionCount(ip=ip, question=question)
        qc.save()
        
        if question.view_cnt:
            question.view_cnt += 1

        else:
            question.view_cnt = 1
            
        question.save()
            
    question =  get_object_or_404(Question, id=question_id)
    

    return render(request, "board/question_detail.html", {"question": question, "page":page, "keyword":keyword, "so":so})

