from django.shortcuts import render, redirect
from .models import Articles


# articles/views.py - index페이지에서 전체 게시글을 조회
def index(request):
    articles = Articles.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    article = Articles.objects.get(pk=pk) # id는 pk라고 써도 괜찮다.
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def form(request):
    return render(request, 'articles/form.html')

def create(request):
    # title = request.GET.get('title')
    # content = request.GET.get('content')

    title = request.POST.get('title')
    content = request.POST.get('content')

    # DB에 새로운 Article 저장
    # Articles.objects.create(
    #     title = title,
    #     content = content
    # )

    article = Articles(title=title, content=content)
    article.save()

    return redirect('articles:index')