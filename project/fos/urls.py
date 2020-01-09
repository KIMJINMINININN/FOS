#하위 url에 속함
from django.urls import path

from . import views # 현재 패키지에서 views 모듈을 가져옴

# ROUTE 따로 관리
urlpatterns = [
    path('home', views.home, name='home'),
]