from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first_bus/', views.first_bus),
    path('second_bus/', views.second_bus),
    path('first_map/', views.first_map),
    path('first_map_data/', views.first_map_data),
    path('firstbus_station_map/', views.firstbus_station_map),
    path('firstbus_station/<int:NUMBER>/', views.firstbus_station),
    path('second_map/', views.second_map),
    path('second_map_data/', views.second_map_data),
    path('infra_map/', views.infra_map),
    path('infra_map_data/', views.infra_map_data),
    path('이용안내/', views.이용안내),
    path('공지사항/', views.공지사항),
    path('bs420번/', views.bs420번),
    path('bs1203번/', views.bs1203번),
    path('불편사항/', views.불편사항),
    path('소개/', views.소개),
    path('자유게시판/', views.자유게시판),
    path('홈/', views.홈),
    path('Q&A/', views.문의),
]
