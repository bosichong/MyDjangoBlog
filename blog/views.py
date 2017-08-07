#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bloglist(request):
    return render(request, 'blog/list.html')

def blog(request, id):
    """blog文章详情页"""
    # return HttpResponse(id)
    return render(request, 'blog/blog.html')