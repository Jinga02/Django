import random
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('안녕하세요!.')

def greeting(request):
    # name 변수 직접 입력
    return render(request, 'greeting.html', {'name' : 'Alice'})

def greeting2(request):
    # 원하는 변수를 생성
    foods = ['apple', 'banana', 'coconut',]
    info = {
        'name' : 'JAEHWAN'
    }
    # 생성한 변수를 context에 넣어 한방에 사용
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'greeting2.html', context) # context에 넣었기때문에 context만 쓰면 됨

def dinner(request):
    foods = ['족발', '햄버거', '치킨', '피자',]
    # python random 함수사용
    pick = random.choice(foods)
    # context에 저장
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'dinner.html', context)

def base(request):
    return render(request, 'base.html')

def child(request):
    return render(request, 'child.html')

