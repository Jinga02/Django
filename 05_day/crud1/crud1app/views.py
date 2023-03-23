from django.shortcuts import render, redirect
from .models import Crud
from .forms import CrudForm

def home(request):
    crud = Crud.objects.all()
    context = {
        'crud' : crud
    }
    return render(request, 'crud1app/home.html', context)

# def form(request):
#     return render(request, 'crud1app/create.html')

def create(request):
    if request.method == 'POST':
        form = CrudForm(request.POST)
        if form.is_valid():
            crud = form.save()
            return redirect('crud1:detail', crud.pk)
        # title = request.POST.get('title')
        # content = request.POST.get('content')
        # crud = Crud.objects.create(
        #     title = title,
        #     content = content
        # )
        # crud.save()
        return redirect('crud1:home')
    else:
        form = CrudForm()
        context = {
            'form' : form
        }
        return render(request, 'crud1app/create.html', context)
    
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

# def edit(request, pk):
#     crud = Crud.objects.get(pk=pk)
#     context = {
#         'crud' : crud
#     }
#     return render(request, 'crud1app/edit.html', context)

def update(request, pk):
    crud = Crud.objects.get(pk=pk)
    if request.method == 'POST':
        form = CrudForm(request.POST, instance=crud)
        if form.is_valid():
            form.save()
            return redirect('crud1:detail', crud.pk)
    else:
        form = CrudForm(instance=crud)
    context = {
        'form' : form,
        'crud' : crud
    }
    return render(request, 'crud1app/update.html', context)