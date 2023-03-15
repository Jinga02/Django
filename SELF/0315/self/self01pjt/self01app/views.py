from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def self01(request):
    return render(request, 'self01app/self01.html')

def self02(request):
    info = {
        'name' : 'JAEHWAN',
        'age' : 27,
    }
    return render(request, 'self01app/self02.html', info)

def self03(request):
    menu = ['떡볶이', '치킨', '피자', '햄버거', '초밥', '족발', '짜장면', '한솥']
    day = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    name = '지은'
    menu_pick = random.choice(menu)
    day_pick = random.choice(day)
    context = {
        'menu' : menu,
        'day' : day,
        'name' : name,
        'menu_pick' : menu_pick,
        'day_pick' : day_pick
    }
    return render(request, 'self01app/self03.html', context)


    
