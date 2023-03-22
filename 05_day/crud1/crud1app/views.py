from django.shortcuts import render, redirect
from .models import Crud

def home(request):
    crud = Crud.objects.all()
    context = {
        'crud' : crud
    }
    return render(request, 'crud1app/home.html', context)

def form(request):
    return render(request, 'crud1app/create.html')

def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')

    crud = Crud.objects.create(
        title = title,
        content = content
    )
    crud.save()

    return redirect('crud1:home')

def detail(request, pk):
    crud = Crud.objects.get(pk=pk)
    context = {
        'crud' : crud
    }
    return render(request, 'crud1app/detail.html', context)

def delete(request, pk):
    crud = Crud.objects.get(pk=pk)
    crud.delete()
    return redirect('crud1:home')

def edit(request, pk):
    crud = Crud.objects.get(pk=pk)
    context = {
        'crud' : crud
    }
    return render(request, 'crud1app/edit.html', context)

def update(request):
    pk = int(request.POST.get('pk'))
    crud = Crud.objects.get(pk=pk)
    crud.title = request.POST.get('title')
    crud.content = request.POST.get('content')
    crud.save()
    return redirect('crud1:detail', crud.pk)