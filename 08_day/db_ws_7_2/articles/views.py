from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer

@api_view(['GET'])
def article_list(request):
    # articles = Article.objects.all()
    # ()안의 값을 가져오거나 에러발생시 404출력
    articles = get_list_or_404(Article)
    serializers = ArticleListSerializer(articles, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def article_detail(request, article_pk):
    articles = Article.objects.get(pk = article_pk)
    serializers = ArticleSerializer(articles)
    return Response(serializers.data, status=status.HTTP_200_OK)


