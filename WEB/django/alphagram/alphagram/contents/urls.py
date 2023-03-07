from django.urls import path
from . import views

urlpatterns = [
    # 컨텐츠 홈
    path("", views.ContentsView.as_view(), name="contents"),
]
