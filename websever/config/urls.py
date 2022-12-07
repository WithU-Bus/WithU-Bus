from django.contrib import admin
from django.urls import include, path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bs1203/', views.bs1203),
    path('bus_station_map/', views.bus_station_map),
    path('bus_station/<int:NUMBER>/', views.bus_station),
    path('bs420/', views.bs420),
    path('infra_map/', views.infra_map),
    path('infra_map_data/', views.infra_map_data),
    path('userinfo/', views.userinfo),
    path('notice/', views.notice),
    path('info/', views.info),
    path('', views.home),
    path('review/', views.review),
    path('Q&A/', views.QandA),
    path('contact/', views.contact),
    path('search/', views.search, name='search'),
]

