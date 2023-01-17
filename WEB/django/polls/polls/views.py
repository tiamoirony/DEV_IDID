from django.shortcuts import render,get_object_or_404,redirect
from .models import Question

from django.views.generic import ListView,DetailView

# Create your views here.
def index(request):
    """
    질문 전체 보기 구현
    """
    # 질문 전체 리스트 : 가장 최신 질문 순으로
    # Question.objects.order_by("pub_date") 오름차순
    question_list = Question.objects.order_by("-pub_date")   # 내림차순
    # question_list = Question.objects.order_by("-pub_date")[:5]   # 내림차순 + 5 개
    return render(request, "polls/index.html", {"question_list":question_list})


def detail(request, pk):
    """
    pk에 해당하는 choice 필요, question 필요

    question = get_object_or_404(Question, pk=pk)
    choices = Choice.objects.filter(question_id=pk)
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, "polls/detail.html", {"question":question})


def votes(request,pk):
    """
    pk에 해당하는 질문 가져오기/사용자의 선택된 choice 가져오기
    질문을 통해 choice 에 접근한 후 투표 수 증가    
    """
    question = get_object_or_404(Question, pk=pk)

    if request.method == "POST":
        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except KeyError as e:
            return render(request, "polls/detail.html", {"question":question, "error_message":"선택하지 않았습니다."})
        else:
            selected_choice.votes += 1
            selected_choice.save()
            return redirect("polls:results",pk=pk)
        
def results(request,pk):
    """
    pk에 해당하는 질문 가져오기
    """
    question = get_object_or_404(Question, pk=pk)
    return render(request, "polls/result.html", {"question":question})


##### 제네릭 뷰
#  
# template_name : 사용할 html 파일 지정
# context_object_name : 모델소문자(DetailView), 모델소문자_list(ListView) ==> 기본값
#                       기본값을 사용하지 않을 것이라면 추가 지정
#
#######################

class IndexView(ListView):
    # model = Question  # Question.objects.all() 와 같은 개념
    template_name = "polls/index.html"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")

class PollDetailView(DetailView):
    template_name = "polls/detail.html"
    model = Question

class PollResultView(DetailView):
    template_name = "polls/result.html"
    model = Question


    
   
