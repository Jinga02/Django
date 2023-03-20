import re
from django.shortcuts import render, redirect
from .models import Article


# Create your views here.
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)\

# 사용자 입력 받는 페이지를 렌더링하자!
def new(request):
    return render(request, 'articles/new.html')

# 입력 데이터를 처리해서 DB에 저장하자!
def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 인스턴스를 생성해서 DB에 저장하는(레코드 생성)
    article = Article(title=title, content=content)
    print(article.created_at)
    print(article.updated_at)
    
    # DB에 저장
    article.save()
    print(article.created_at)
    print(article.updated_at)
    
    # redirect가 일어날때 뒤의 경로로 자동이동
    return redirect('articles:index')

def detail(request, pk):
    # pk값으로 데이터를 조회(pk값은 variable routing으로 받은 정보)
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    # pk에 해당되는 게시판 글 하나 정보를 가져오기
    article = Article.objects.get(pk=pk)
    #인스턴스 DB레코드 삭제
    article.delete()
    return redirect('articles:index')

def edit(request, pk):
    # 해당 게시글에 대한 정보를 조회하고,
    # 그 정보로 이루어진 입력폼을 구성하겠다.
    article = Article.objects.get(pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request):
    # 해당 게시글 pk, 제목, 내용
    # 해당 게시글 정보를 DB에서 가져온다.
    pk = int(request.POST.get('pk'))
    article = Article.objects.get(pk=pk)
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)
