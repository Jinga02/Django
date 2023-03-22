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
    title = request.POST.get('title')
    content = request.POST.get('content')
    crud3 = crud3class(title=title, content=content)
    crud3.save()
    return redirect('crud3:home')

def detail(request, pk):
    crud3 = crud3class.objects.get(pk=pk)
    context = {
        'crud3' : crud3
    }
    return render(request, 'crud3app/detail.html', context)

def delete(request, pk):
    crud3 = crud3class.objects.get(pk=pk)
    crud3.delete()
    return redirect('crud3:home')

def edit(request, pk):
    crud3 = crud3class.objects.get(pk=pk)
    context = {
        'crud3' : crud3
    }
    return render(request, 'crud3app/edit.html', context)

def update(request):
    pk = int(request.POST.get('pk'))
    crud3 = crud3class.objects.get(pk=pk)
    crud3.title = request.POST.get('title')
    crud3.content = request.POST.get('content')
    crud3.save()
    return redirect('crud3:detail', crud3.pk)

    