from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
# from rest_framework.permissions import IsAuthenticated, IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Article, Comment, Category
from .serializers import CommentSerializer, ArticleSerializer, ArticleListSerializer, CategorySerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from django.contrib.auth.admin import 
from django.contrib.auth import get_user_model

# Create your views here.
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticatedOrReadOnly])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        category = Category.objects.get(pk=request.data.get('category'))
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, category=category)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(['GET', 'DELETE', 'PUT'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        category = Category.objects.get(pk=request.data.get('category'))
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(category=category)
            return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
# @authentication_classes([TokenAuthentication])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
@authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
# @authentication_classes([TokenAuthentication])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@authentication_classes([TokenAuthentication])
# @permission_classes([IsAdminOrReadOnly])
@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def category_management(request, category_pk):
    category = get_object_or_404(Category, pk=category_pk)

    if request.method == 'PUT':
        serializer = CategorySerializer(category, data=request.data, partial=True)  # 
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)