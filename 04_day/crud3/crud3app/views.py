from django.shortcuts import render, redirect
from .models import crud3class

# Create your views here.
def home(request):
    crud3 = crud3class.objects.all()
    context = {
        'crud3' : crud3
    }
    return render(request, 'crud3app/home.html', context)

def form(request):  # DB에 전송 할 함수
    return render(request, 'crud3app/form.html')

def create(request):    # DB에 저장하기 위한 함수
    title = request.GET.get('title')
    content = request.GET.get('content')
    crud3 = crud3class(title=title, content=content)
    crud3.save()
    return redirect('crud3app:home')