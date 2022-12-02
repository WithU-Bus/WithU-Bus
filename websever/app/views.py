from django.http import HttpResponse
from django.shortcuts import render
from app.models import Bus
from app.models import Infra

def bs1203번(request):
    firstbus = Bus.objects.filter(BUS='1203')
    return render(request, 'app/1203번.html', {
        'my_data' : firstbus,
    })

def bs420번(request):
    secondbus = Bus.objects.filter(BUS='420')
    return render(request, 'app/420번.html', {
        'my_data' : secondbus,
    })

def bus_station(request, NUMBER):
    station = Bus.objects.get(NUMBER=NUMBER)
    context = {
        'station' : station,
    }
    return render(request, 'app/bus_station.html', context) 

def bus_station_map(request):
    return render(request, 'app/bus_station_map.html')  


def infra_map(request):
    return render(request, 'app/bus_station_map.html')

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
def 소개(request):
    return render(request, 'app/소개.html')
def 한줄후기(request):
    return render(request, 'app/한줄후기.html')
def 홈(request):
    return render(request, 'app/홈.html')
def 문의(request):
    return render(request, 'app/Q&A.html')

#Q&A
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        # 발신자주소, 수신자주소, 메시지
        send_mail('WithU.Bus@gmail.com', email, name, comment)
        return render(request, 'app/홈.html')
    return render(request, 'app/contact.html')


import smtplib #메일을 보내기 위한 SMTP 관련 모듈
from email.mime.text import MIMEText

def send_mail(from_email, to_email, name, msg):
    smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465) # 구글에서 제공하는 SMTP 서버 접속 설정
    smtp.login(from_email, 'lczjrtpmgdtwrjjc') # 인증정보 설정
    #MIMEText('메시지',('메시지 형식'),('문자열 타입'))
    name = name
    msg = MIMEText(msg)
    msg['Subject'] = '[불편사항]' + '[작성자]' + name + '[회신메일]' + to_email # 제목([불편사항]접수자 이메일주소)
    msg['To'] = from_email # 수신 이메일(받는사람 이메일 주소)
    smtp.sendmail(from_email, from_email, msg.as_string())
    smtp.quit()

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']        
        bus = Bus.objects.filter(NAME__contains=searched)
        return render(request, 'app/searched.html', {'searched': searched, 'bus': bus})
    else:
        return render(request, 'app/searched.html', {})