from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer
# Create your views here.
def article_html(request):
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, 'articles/article.html', context)

# from django.http.response import JsonResponse

def article_json_1(request):
    articles = Article.objects.all()
    articles_json = []

    for article in articles:
        articles_json.append(
            {
            'id' : article.pk,
            'title' : article.title,
            'content' : article.content,
            'created_at' : article.created_at,
            'updated_at' : article.updated_at,
            }
        )
    # JSON을 담은 파일이라 JsonResponse로 전송해야한다.
    # 'safe' parameter 
    # 기본 값은 True이다. True시 dict 인스턴스만 허용한다.
    # False로 설정 시 모든 타입의 객체를 serialization 할 수 있다.
    return JsonResponse(articles_json, safe=False)

# from django.http.response import JsonResponse, HttpResponse
# from django.core import serializers

def article_json_2(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    # serializers 직렬활
    # 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를
    # 나중에 재구성할 수 있는 포맷으로 변환하는 과정
    # 어떤 언어나 환경에서도 나중에 다시 쉽게 사용할 수 있는 포맷으로 변환하는 과정
    return HttpResponse(data, content_type='application/json')
    

from .serializers import ArticleSerializer

@api_view(['GET'])
def article_json_3(request):
    articles = Article.objects.all()
    serializers = ArticleSerializer(articles, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    # 기본적으로 중복 표현은 None 값을 받고자 하는 경우 required=False를 추가해야 한다.
    # 중복 표현 값에 대해 list로 받고자 하는 경우, many=True를 추가한다.
    serializers = ArticleSerializer(articles, many=True)
    # 인스턴스를 반환하는게 아니라 데이터를 반환하기 때문에
    return Response(serializers.data)

@api_view(['GET'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    serializer = ArticleSerializer(article) # 1개만 가져 올 거라
    return Response(serializer.data)