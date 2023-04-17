from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleDetailSerializer, CommentSerializer

from rest_framework import status
from django.shortcuts import get_list_or_404, get_object_or_404

# 요청에 따라 무엇을 하려는지 정해져 있고, 또 알 수 있기 때문에
# 지금까지와는 다르게 list에 함수 작성

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # articles = Article.objects.all()
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # serializer인데 data가 들어가 있는 serializer
        serializer = ArticleListSerializer(data=request.data)
        # raise_exception=True을 통해 유효성검사 실패시 알아서 400코드 표시해줌
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # rest_framework 의 status에서 상태코드를 제공해줌.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        serializer = ArticleDetailSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        # 담아 줄 데이터가 없고 삭제해야 하기 때문에 data는 미작성
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleDetailSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # status 생략 시 자동으로 200반환
            return Response(serializer.data)
        
# @api_view(['GET'])
# def comment_list(request):
#     comments = Comment.objects.all()
#     serializer = CommentSerializer(comments, many=True)
#     return Response(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method=='GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method=='DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method=='PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['GET', 'POST'])
# 어떤 게시글의 댓글인지 확인이 필요하기때문에 따로 작성
def comment_list(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # save()메서드는 특정 serializer 인스턴스를 저장하는 과정에서 추가적인 데이터를 받을 수 있다.
            # CommentSerializer를 통해 serialize되는 과정에서 Parameter로 넘어온 article_pk에 해당하는 
            # article 객체를 추가적인 데이터를 넘겨 저장
            serializer.save(article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == 'GET':
        comments = article.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)