#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger#翻页相关模块
from django.db.models import Q#模糊查询多个字段使用


from .models import Article, Category, UserProfile, Siteinfo
from .forms import Searchform, Tagform
# Create your views here.

def bloglist(request):
    articles = Article.objects.filter(article_type='2').order_by('-article_create_time')
    page_number = int(request.GET.get('p', '1'))#获取当前页码，用来控制翻页中当前页码的class="{% if p == page_number %}am-active {% endif %}"
    c =request.GET.get('c', '')#分类
    s = ''#搜索关键字
    t = ''#TAG关键字
    if request.method == 'GET':
        form = Searchform(request.GET)
        if form.is_valid():
            s =request.GET.get('s')

    if request.method == 'GET':
        form = Tagform(request.GET)
        if form.is_valid():
            t =request.GET.get('t')
    if c:
        articles = articles.filter(article_category=c, article_type='2').order_by('-article_create_time')
    elif s:
        articles = articles.filter(Q(article_title__contains=s)|Q(article_content__contains=s),article_type='2').order_by('-article_create_time')
    elif t:
        articles = articles.filter(article_tag__contains=t, article_type='2').order_by('-article_create_time')#name__contains 模糊查找字段
        

    
    paginator = Paginator(articles, 2) # 第二个参数是每页显示的数量
    page = request.GET.get('p')          # 获取URL参数中的page number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:                # 若不是整数则跳到第一页
        contacts = paginator.page(1)
    except EmptyPage:                       # 若超过了则最后一页
        contacts = paginator.page(paginator.num_pages)

    page_url = request.get_full_path()

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
                                    'page_url':page_url,
                                    'page_number':page_number,
                                    'form':form})


def blog(request, id):
    """blog文章详情页"""
    article = Article.objects.get(pk=id)#日志数据
    
    #检测上一篇 下一篇文章
    try:
        pa = Article.objects.get(pk=int(id)-1)#前一篇日志
        if pa.article_type != '2':
            pa = None
    except Exception as e:
        pa = None

    
    try:
        na = Article.objects.get(pk=int(id)+1)#下篇日志
        if na.article_type != '2':
            na = None
    except Exception as e:
        na = None
    
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    categorys = Category.objects.all()#获取所有分类
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    tags = article.article_tag.split()#获得日志的tag


    if article.article_type != '2':
        return render(request, '404.html')
    else:
        return render(request, 'blog/blog.html', {
                                    'article':article, 
                                    'pa':pa,
                                    'na':na,
                                    'tags':tags, 
                                    'userinfo':userinfo,
                                    'categorys':categorys,
                                    'siteinfo':siteinfo,})


