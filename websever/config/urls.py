from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bs1203번/', views.bs1203번),
    path('bs1203번_station_map/', views.bs1203번_station_map),
    path('bs1203번_station/<int:NUMBER>/', views.bs1203번_station),
    path('bs420번/', views.bs420번),
    path('bs420번_station_map/', views.bs420번_station_map),
    path('bs420번_station/<int:NUMBER>/', views.bs420번_station),
    path('infra_map/', views.infra_map),
    path('infra_map_data/', views.infra_map_data),
    path('이용안내/', views.이용안내),
    path('공지사항/', views.공지사항),
    path('bs420번/', views.bs420번),
    path('불편사항/', views.불편사항),
    path('소개/', views.소개),
    path('', views.홈),
    path('홈/', views.홈),
    path('자유게시판/', views.자유게시판),
    path('Q&A/', views.문의),
]

