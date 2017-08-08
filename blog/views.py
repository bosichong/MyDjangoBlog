#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse


from .models import Article, Category, UserProfile, Siteinfo
# Create your views here.

def bloglist(request):
    return render(request, 'blog/list.html')

def blog(request, id):
    """blog文章详情页"""
    article = Article.objects.get(pk=id)#日志数据
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    categorys = Category.objects.all()#获取所有分类
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    tags = article.article_tag.split()
    return render(request, 'blog/blog.html', {
                                    'article':article, 
                                    'tags':tags, 
                                    'userinfo':userinfo,
                                    'categorys':categorys,
                                    'siteinfo':siteinfo,})


