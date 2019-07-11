from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import BS, BS2, Cost
from .forms import BSForm, BS2Form, CostForm
import googlemaps
import pandas as pd
import numpy as np
import math
from haversine import haversine
from IPython import embed
import os
from django.conf import settings

def intro(request):
    # histories = BS.objects.all()[::-1]
    histories = BS.objects.order_by('-pk')
    context = {'histories': histories}
    return render(request, 'bs/intro.html', context)

@login_required
def new(request):
    # bs_map = get_object_or_404(BS, pk=history_pk) # 객체
    bs_map = BS.objects.order_by('-pk') # 쿼리셋
    counter = []
    if request.method == 'POST':
        form = BSForm(request.POST)
        if form.is_valid():
            history = form.save(commit=False)
            history.user = request.user
            mem_count = history.member
            history.save()
            for i in range(1, mem_count+1):
                counter.append(i)
            context = {
                'bs_map': bs_map,
                'counter': counter
            }
            return render(request,'bs/map_1.html', context)
    else:
        form = BSForm()
    context = {'form': form}
    return render(request, 'bs/form.html', context)

# def map_1(request, history_pk):
#     bs_map = get_object_or_404(BS, pk=history_pk)
#     if request.method == 'POST':
#         form = BS2Form(request.POST)
#         if form.is_valid():
#             history = form.save(commit=False)
#             history.user = request.user
#             history.save()
#             # context = {'bs_map':bs_map}
#             return redirect('bs:match', history.pk)
#     else:
#         form = BS2Form()
#     context = {'form': form, 'counter': range(1, bs_map.member+1)}
#     return render(request, 'bs/map_1.html', context)
#     # return render(request, 'bs/form.html', context)

def map_1(request):
    gmaps_key = "*****"
    gmaps = googlemaps.Client(key=gmaps_key)
    lat_sum = 0
    lng_sum = 0
    user_lat = []
    user_lng = []

    start = request.POST.getlist('start[]')
    weight = request.POST.getlist('weight[]')
    sum_weight = 0
    for i in weight:
        sum_weight += int(i)


    match_mem = len(start) # 인원수(member)

    for i in start:
        user_info = gmaps.geocode(i, language='ko')
        user_geo = user_info[0].get('geometry')
        user_lat.append(user_geo['location']['lat'])  # 사용자가 입력한 위치의 위도값의 집합
        user_lng.append(user_geo['location']['lng'])  # 사용자가 입력한 위치의 경도값의 집합

    for i in range(match_mem):
        lat_sum += float(user_lat[i]) * float(weight[i])
        lng_sum += float(user_lng[i]) * float(weight[i])

    lat_avg = lat_sum / sum_weight
    lng_avg = lng_sum / sum_weight
    match1 = (lat_avg, lng_avg) # 1차 매칭 위치의 경위도값


    # 지하철역 출력
    station_name = []  # 지하철역 집합 리스트
    station = pd.read_excel(os.path.join(settings.BASE_DIR, 'subway_all.xlsx'), encoding='utf-8')['역이름']
    for name in station:
        station_name.append(name + '역')

    # 지하철역과 사용자의 평균 위치의 차이 출력
    dic_all = []  # 거리 차이의 집합 리스트
    # for i in station_name: # 전체 600개
    for i in station_name: # 테스트용 100개
        try:
            station_info = gmaps.geocode(i, language='ko')
            station_geo = station_info[0].get('geometry')
            station_lat = station_geo['location']['lat']  # 위도
            station_lng = station_geo['location']['lng']  # 경도
            station_loc = (station_lat, station_lng)  # 위도, 경도를 담은 튜플
            distance = haversine(match1, station_loc)  # 사용자들의 평균 위치와 역 간의 거리
            dic_all.append(distance) # 거리 차의 집합
        except IndexError:
            if i == '동대문역':
                station_lat = 37.571697
                station_lng = 127.01086
                station_loc = (station_lat, station_lng)  # 위도, 경도를 담은 튜플
                distance = haversine(match1, station_loc)  # 사용자들의 평균 위치와 역 간의 거리
                dic_all.append(distance)
            elif i == '삼양역':
                station_lat = 37.626985
                station_lng = 127.018141
                station_loc = (station_lat, station_lng)  # 위도, 경도를 담은 튜플
                distance = haversine(match1, station_loc)  # 사용자들의 평균 위치와 역 간의 거리
                dic_all.append(distance)
            else:  # 4.19 묘지역
                station_lat = 37.64942
                station_lng = 127.013708
                station_loc = (station_lat, station_lng)  # 위도, 경도를 담은 튜플
                distance = haversine(match1, station_loc)  # 사용자들의 평균 위치와 역 간의 거리
                dic_all.append(distance)

    x = dict(zip(station_name, dic_all)) # {'지하철역': 역과 1차 매칭 지점 간의 거리 차이}
    sort = sorted(x.items(), key=lambda t: t[1])[0:5] # 가까운 순으로 5곳의 지하철역 출력


    best = BS2()
    # start -> 리스트 [강남역, 역삼역]
    start.append("center")
    # start -> 리스트 [강남역, 역삼역, center]
    # user_lat # 리스트 [강남역 위도, 역삼역 위도]
    # user_lng # 리스트 [강남역 경도, 역삼역 경도]
    user_lat.append(lat_avg) # 리스트 [강남역 위도, 역삼역 위도, 중심지점 위도]
    user_lng.append(lng_avg) # 리스트 [강남역 경도, 역삼역 경도, 중심지점 경도]


    for i in range(len(sort)):
        start.append(sort[i][0])
        # 리스트[강남역, 역삼역, center, 역이름 1 ~ 5]
        user_lat.append(gmaps.geocode(sort[i][0], language='ko')[0].get('geometry')['location']['lat'])
        # 리스트 [강남역 위도, 역삼역 위도, 중심지점 위도, 위도 1 ~ 5]
        user_lng.append(gmaps.geocode(sort[i][0], language='ko')[0].get('geometry')['location']['lng'])
        # 리스트 [강남역 경도, 역삼역 경도, 중심지점 경도, 경도 1 ~ 5]

    sort_name = start[-6:] # [center, 역이름 1 ~ 5]
    sort_lat = user_lat[-6:]  # [center, 역 1 ~ 5 위도]
    sort_lng = user_lng[-6:]  # [center, 역 1 ~ 5 경도]
    start_lat = user_lat[:-7] # [강남역 위도, 역삼역 위도]
    start_lng = user_lng[:-7] # [강남역 경도, 역삼역 경도]
    best.start = start # [강남역, 역삼역, center, 역이름 1 ~ 5]
    best.weight = weight # [1, 1]
    best.goal_lat = user_lat # [강남역 위도, 역삼역 위도, 중심지점 위도, 위도 1 ~ 5]
    best.goal_lng = user_lng # [강남역 경도, 역삼역 경도, 중심지점 경도, 경도 1 ~ 5]


    context = {
        'best': best,
        'sort_name': sort_name,
        'sort_lat': sort_lat,
        'sort_lng': sort_lng,
        'center_lat': user_lat[-6],
        'center_lng': user_lng[-6],
        'start_lat': user_lat[:-7],
        'start_lng': user_lng[:-7],
    }
    return render(request, 'bs/map_2.html', context)

    # for i in range(len(sort)):
    #     sort_info = gmaps.geocode(f'sort[i][0]', language='ko')
    #     sort_geo = sort_info[0].get('geometry')
    #     sort_lat = sort_geo['location']['lat']  # 위도
    #     sort_lng = sort_geo['location']['lng']  # 경도
    #     start.append(sort[i][0])

# def map_1(request):
#     if request.method == 'POST':
#         form = BS2Form(request.POST)
#         if form.is_valid():
#             history = form.save(commit=False)
#             history.save()
#             return render(request, 'bs/map_2.html')
#     else:
#         form = BS2Form()
#     context = {'form': form}
#     return render(request, 'bs/form.html', context)

# def center(x,y):
#     gmaps_key = "AIzaSyCYmb7K-OhKPh2JlvpRQKhYOnoIqCcKUSw"
#     gmaps = googlemaps.Client(key=gmaps_key)
#     lat_sum = 0
#     lng_sum = 0
#     weight = []
#     person = []
#     for i in map_1.history.member:
#         start_info = gmaps.geocode(person[i], language='ko')
#         start_geo = start_info[0].get('geometry')
#         start_lat = start_geo['location']['lat']
#         start_lng = start_geo['location']['lng']
#         lat_sum += start_lat * weight[i]
#         lng_sum += start_lng * weight[i]
#         # print(f'{i + 1}번 사용자', person[i], "위도: ", start_lat, "경도: ", start_lng)
#         # print('-----------------------------------------------')
#
#     lat_avg = lat_sum / sum(weight)
#     lng_avg = lng_sum / sum(weight)
#     center = (lat_avg, lng_avg)
#     # print('평균 위치:', loc_avg)  # 사용자들의 평균 위도&경도


def map_2(request, history_pk):
    history3 = get_object_or_404(BS2, pk=history_pk)
    request.POST.get()
    history3.save()
    context = {'history3': history3}
    return render(request, 'bs/form.html', context)


def detail(request, history_pk):
    history = get_object_or_404(BS, pk=history_pk)
    context = {'history':history}
    return render(request, 'bs/detail.html', context)

def update(request, history_pk):
    history = get_object_or_404(BS, pk=history_pk)
    if request.method == 'POST':
        form = BSForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('bs:detail', history.pk)
    else:
        form = BSForm(instance=history)
    context = {'form':form, 'history':history}
    return render(request, 'bs/form.html', context)

def delete(request, history_pk):
    history = get_object_or_404(BS, pk=history_pk)
    if request.method == 'POST':
        history.delete()
        return redirect('bs:intro')
    else:
        return redirect('bs:detail')

def calculate(request, history_pk):
    history = get_object_or_404(BS, pk=history_pk)
    if request.method == 'POST':
        form = CostForm(request.POST, instance=history)
        if form.is_valid():
            form.save()
            return redirect('bs:calculate', history.pk)
    else:
        form = CostForm(instance=history)
    context = {'form':form, 'history':history}
    return render(request, 'bs/calculate.html', context)