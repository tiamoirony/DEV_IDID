from django.urls import path
from django.views.generic import TemplateView
from . import views

# 하나의 프로젝트 안에 여러 개의 앱이 존재하는 개념
# 서로 다른 앱 안에 동일한 이름을 사용할 수 있음 => 구별하는 방법은 app_name 을 통해서
# polls:index , users:index 처럼 사용
app_name = "polls"

urlpatterns = [
    # html 페이지만 띄우면 될 때
    # path('',TemplateView.as_view(template_name="polls/index.html"),name="index"),
    #### 함수형 뷰 ####
    # path('',views.index,name="index"),
    # # /polls/1/
    # path('<int:pk>/',views.detail, name="detail"),
    # # /polls/1/vote/
    # path('<int:pk>/vote/',views.votes, name="vote"),
    # # /polls/1/results/
    # path('<int:pk>/results/',views.results, name="results"),
    #### 클래스 뷰 ####
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.PollDetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.PollResultView.as_view(), name="results"),
    path("<int:pk>/vote/", views.votes, name="vote"),
]
