from django.http import HttpResponse
from django.shortcuts import render
from app.models import Firstbus
from app.models import Secondbus
from app.models import Infra

def bs1203번(request):
    firstbus = Firstbus.objects.all()
    return render(request, 'app/1203번.html', {
        'my_data' : firstbus,
    })

def bs1203번_station(request, NUMBER):
    station = Firstbus.objects.get(NUMBER=NUMBER)
    context = {
        'station' : station,
    }
    return render(request, 'app/1203번_station.html', context) 

def bs1203번_station_map(request):
    return render(request, 'app/1203번_station_map.html')  

def bs420번(request):
    secondbus = Secondbus.objects.all()
    return render(request, 'app/420번.html', {
        'my_data' : secondbus,
    })

def bs420번_station(request, NUMBER):
    station = Secondbus.objects.get(NUMBER=NUMBER)
    context = {
        'station' : station,
    }
    return render(request, 'app/420번_station.html', context) 

def bs420번_station_map(request):
    return render(request, 'app/420번_station_map.html') 

def infra_map(request):
    return render(request, 'app/1203번_station_map.html')

from django.http import JsonResponse
from django.forms.models import model_to_dict

import math
def distance(lat1, lng1, lat2, lng2) :
    theta = lng1 - lng2
    dist1 = math.sin(deg2rad(lat1)) * math.sin(deg2rad(lat2))
    dist2 = math.cos(deg2rad(lat1)) * math.cos(deg2rad(lat2))
    dist2 = dist2* math.cos(deg2rad(theta))
    dist = dist1 + dist2
    dist = math.acos(dist)
    dist = rad2deg(dist) * 60 * 1.1515 * 1.609344
    return dist

def deg2rad(deg):
    return deg * math.pi / 180.0
def rad2deg(rad):
    return rad * 180.0 / math.pi

def infra_map_data(request):
    data = Infra.objects.all()
    lat = request.GET.get('lat')
    lng = request.GET.get('lng')
    map_list = []
    for d in data:
        d = model_to_dict(d)
        dist = distance(float(lat), float(lng), d['lat'], d['lng'])
        if(dist<=0.8):
            map_list.append(d)
            
    return JsonResponse(map_list, safe=False)

def 이용안내(request):
    return render(request, 'app/이용안내.html')  
def 공지사항(request):
    return render(request, 'app/공지사항.html')
def 불편사항(request):
    return render(request, 'app/불편사항.html') 
def 소개(request):
    return render(request, 'app/소개.html')
def 자유게시판(request):
    return render(request, 'app/자유게시판.html')
def 홈(request):
    return render(request, 'app/홈.html')
def 문의(request):
    return render(request, 'app/Q&A.html')