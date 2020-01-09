#하위 url에 속함
from django.urls import path

from . import views # 현재 패키지에서 views 모듈을 가져옴

# ROUTE 따로 관리
urlpatterns = [
    path('index', views.index, name='index'),
    path('basic-table', views.basic-table, name='basic-table'),
    path('blank', views.blank, name='blank'),
    path('buttons', views.buttons, name='buttons'),
    path('chart', views.chart, name='chart'),
    path('charts', views.charts, name='charts'),
    path('compose', views.compose, name='compose'),
    path('datatable', views.datatable, name='datatable'),
    path('forms', views.forms, name='forms'),
    path('google-maps', views.google-maps, name='google-maps'),
    path('vector-maps', views.vector-maps, name='vector-maps'),
    path('ui', views.ui, name='ui'),
]