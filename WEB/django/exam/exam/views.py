from django.shortcuts import render, redirect, get_object_or_404
from .forms import NameForm, MusicianForm
from .models import Musician

# 함수형 뷰


def index(request):
    return render(request, "exam/index.html")


def custom_form(request):
    """
    get / post  - Form 클래스 없이
    """

    errors = []

    if request.method == "POST":
        # name 가져오기
        name = request.POST["name"]  # request.POST.get("name")
        print(name)

        # 유효성 검증 - 이름이 홍길동이어야 한다.
        if name != "홍길동":
            # 에러메세지 전송 - 원래 페이지로 돌려보내기
            errors.append("이름을 확인해 주세요")
        else:
            return redirect("index")

    return render(request, "exam/custom_form.html", {"errors": errors})


def django_form(request):
    """
    get / post  - Form 클래스 사용
    """

    if request.method == "POST":
        # 사용자의 입력값을 폼 데이터로 수신
        form = NameForm(request.POST)
        if form.is_valid():  # 바인딩여부, max_length, required 검증
            return redirect("index")

    else:  # get방식
        # 빈 폼을 하나 생성 후 전송
        form = NameForm()

    return render(request, "exam/django_form.html", {"form": form})


# musician 추가
def musician_create(request):
    """
    get : 비어있는 폼 보여주기
    post : 넘어오는 데이터 폼에 바인딩하기
    """
    if request.method == "POST":
        # 데이터 가져와서 바인딩
        form = MusicianForm(request.POST)
        # 유효성 검증-이상이 없다면 index로 이동
        if form.is_valid():  # bound여부, max_length, blank,null=>False
            form.save()
            return redirect("index")
    else:
        form = MusicianForm()

    return render(request, "exam/create.html", {"form": form})


# musician 삭제
def musician_remove(request, pk):
    musician = get_object_or_404(Musician, pk=pk)

    musician.delete()

    return redirect("musician_function_list")


def musician_edit(request, pk):

    musician = get_object_or_404(Musician, pk=pk)  # 조회

    if request.method == "POST":
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            musician = form.save()
            return redirect(request, "musician_function_detail", {"form": form})
    else:
        form = MusicianForm(instance=musician)

    return render(request, "exam/edit.html", {"form": form})


# musician 전체조회
def musician_list(request):
    """
    전체 musician 추출 후 전송
    """
    # all
    list = Musician.objects.all()

    # render
    return render(
        request, "exam/list.html", {"list": list}
    )  # {"list":list}를 가지고 가야 루프를 돌린다.


# musician 한명조회
def musician_detail(request, pk):
    """
    몇번째? 사람을 자세히 볼건지.. pk 가져와야한다
    pk에 해당하는 musician 조회 후 전송
    ① 조회, 전송 => 템플릿 파일을 처음부터 디자인
    ② 조회, form 담기, 전송 => 템플릿 파일에서 form.as_p or for문 돌려서 만들기
    """
    musician = get_object_or_404(Musician, pk=pk)  # 조회

    form = MusicianForm(instance=musician)  # form 담기

    # return render(request,"exam/detail.html",{"musician":musician}) # 전송
    return render(request, "exam/detail.html", {"form": form})  # form 담아 전송


# 추가
## 클래스 뷰
# TemplateView == render()
# RedirectView == redirect()
# ListView     == 모델 설정
# Detail View


from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class SampleView(TemplateView):
    template_name = "exam/sample.html"


class MusicianListView(ListView):
    model = Musician
    template_name = "exam/list.html"
    context_object_name = "list"  # 기본값 'musician_list'


class MusicianDetailView(DetailView):
    model = Musician
    template_name = "exam/musician_detail.html"
    context_object_name = "musician"


class MusicianCreatelView(CreateView):
    template_name = "exam/create.html"
    form_class = MusicianForm
    success_url = reverse_lazy("musician_class_list")


class MusicianUpdatelView(UpdateView):
    template_name = "exam/edit.html"
    model = Musician
    fields = "__all__"
    context_object_name = "form"

    # 성공시  pk를 가지고 detail로 이동
    # 부모의 get_success_url 재정의

    def get_success_url(self) -> str:
        return reverse_lazy("musician_class_detail", args=[self.object.pk])


class MusicianDeleteView(DeleteView):

    model = Musician
    success_url = reverse_lazy("musician_class_list")

    # get 오버라이딩
    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)
