#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


from .models import Article, Category, UserProfile
# Create your views here.

def bloglist(request):
    return render(request, 'blog/list.html')

def blog(request, id):
    """blog文章详情页"""
    article = Article.objects.get(pk=id)
    return render(request, 'blog/blog.html', {'article':article})