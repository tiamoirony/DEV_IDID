from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name='index.html'),name='index'),
    path("app1/", include('app1.urls')),
    path("app2/", include('app2.urls')),
    path("user/", include('users.urls')),
    
    # path("accounts/", include('django.contrib.auth.urls')),
    
    
]