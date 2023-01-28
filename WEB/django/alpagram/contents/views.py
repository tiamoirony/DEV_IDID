from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

    def dispatch(self, request, *args, **kwargs):
        """
        client 요청이 들어왔을 때 로그인 정보가 있다면 contents 이동 
        없다면 원래대로 home
        """
        if not request.user.is_anonymous:
            return redirect("contents")

        return super().dispatch(request, *args, **kwargs)
    

class ContentsView(TemplateView):
    template_name = "contents/main.html"