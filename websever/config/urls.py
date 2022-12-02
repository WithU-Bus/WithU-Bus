from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bs1203번/', views.bs1203번),
    path('bus_station_map/', views.bus_station_map),
    path('bus_station/<int:NUMBER>/', views.bus_station),
    path('bs420번/', views.bs420번),
    path('infra_map/', views.infra_map),
    path('infra_map_data/', views.infra_map_data),
    path('이용안내/', views.이용안내),
    path('공지사항/', views.공지사항),
    path('bs420번/', views.bs420번),
    path('소개/', views.소개),
    path('', views.홈),
    path('홈/', views.홈),
    path('한줄후기/', views.한줄후기),
    path('Q&A/', views.문의),
    path('contact/', views.contact),
    path('search/', views.search, name='search'),
]

