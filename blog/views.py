#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#翻页相关模块
from django.db.models import Q#模糊查询多个字段使用


from .models import Article, Category, UserProfile, Siteinfo
from .forms import Searchform
# Create your views here.

def bloglist(request):
    articles = Article.objects.filter(article_type='2').order_by('-article_create_time')
    c =request.GET.get('c', '')
    s = ''
    if request.method == 'GET':
        form = Searchform(request.GET)
        if form.is_valid():
            s =request.GET.get('s')
    if c:
        articles = articles.filter(article_category=c).order_by('-article_create_time')
    elif s:
        articles = articles.filter(Q(article_title__contains=s)|Q(article_content__contains=s)).order_by('-article_create_time')
        

    
    paginator = Paginator(articles, 2) # 第二个参数是每页显示的数量
    page = request.GET.get('p')          # 获取URL参数中的page number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:                # 若不是整数则跳到第一页
        contacts = paginator.page(1)
    except EmptyPage:                       # 若超过了则最后一页
        contacts = paginator.page(paginator.num_pages)



    userinfo = UserProfile.objects.get(pk=1)#站长资料
    categorys = Category.objects.all()#获取所有分类
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    return render(request, 'blog/list.html', {'articles':articles, 
                                    'userinfo':userinfo,
                                    'categorys':categorys,
                                    'siteinfo':siteinfo,
                                    'contacts':contacts,
                                    'c':c,
                                    's':s,
                                    'form':form})


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


