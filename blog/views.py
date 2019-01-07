# coding=utf-8
from datetime import *

from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 翻页相关模块
from django.db.models import Q  # 模糊查询多个字段使用

from .models import Article, Category, UserProfile, Siteinfo
from .forms import Searchform, Tagform


# Create your views here.

def bloglist(request):
    articles = Article.objects.filter(article_type='2').order_by('-article_create_time')
    # 获取当前页码，用来控制翻页中当前页码的class="{% if p == page_number %}am-active {% endif %}"
    c = request.GET.get('c', '')  # 分类
    page_number = int(request.GET.get('p', '1'))
    s = ''  # 搜索关键字
    t = ''  # TAG关键字
    d = request.GET.get('d', '')  # 默认文章归档

    if request.method == 'GET':
        form = Searchform(request.GET)
        if form.is_valid():
            s = request.GET.get('s')

    if request.method == 'GET':
        form = Tagform(request.GET)
        if form.is_valid():
            t = request.GET.get('t')
    if c:
        # 分类页
        articles = articles.filter(article_category=c, article_type='2').order_by('-article_create_time')
    elif s:
        # 搜索结果
        articles = articles.filter(Q(article_title__contains=s) | Q(article_content__contains=s),
                                   article_type='2').order_by('-article_create_time')
    elif t:
        # 标签页搜索结果
        articles = articles.filter(article_tag__contains=t, article_type='2').order_by(
            '-article_create_time')  # name__contains 模糊查找字段
    elif d:
        # 文章归档 创建时间对象，然后取年，月，利用filter来取相关时间的日志。
        md = datetime.strptime(d, "%Y-%m")
        articles = articles.filter(article_create_time__year=md.year, article_create_time__month=md.month,
                                   article_type='2')

    paginator = Paginator(articles, 8)  # 第二个参数是每页显示的数量
    page = request.GET.get('p')  # 获取URL参数中的page number
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:  # 若不是整数则跳到第一页
        contacts = paginator.page(1)
    except EmptyPage:  # 若超过了则最后一页
        contacts = paginator.page(paginator.num_pages)
    #优化数据翻页
    pages = pagesHelp(page,paginator.num_pages,6)

    # print(pages)

    page_url = request.get_full_path()

    return render(request, 'blog/list.html', {'articles': articles,
                                              'contacts': contacts,
                                              'c': c,
                                              's': s,
                                              'd': d,
                                              't': t,
                                              'page_url': page_url,
                                              'page_number': page_number,
                                              'form': form,
                                              'pages':pages,})
def pagesHelp(page,num_pages,maxpage):
    '''
    Paginator Django数据分页优化
    使数据分页列表处显示规定的页数
    :param page: 当前页码
    :param num_pages: 总页数
    :param maxpage: 列表处最多显示的页数
    :return:
    '''

    if page is None:#首页时page=None
        p=1
    else:
        p = int(page)
    offset = num_pages-p
    if offset <= maxpage:
        # 结果小于规定数
        return [i + 1 for i in range(num_pages - maxpage, num_pages)]
    elif p <= maxpage:
        # 当前页数小于规定数
        return [i + 1 for i in range(maxpage)]
    else:
        # 正常页数分配
        return [i + 1 for i in range(p - int(maxpage / 2), p + int(maxpage / 2))]




def blog(request, id):
    """blog文章详情页"""
    article = Article.objects.get(pk=id)  # 日志数据
    article.increase_article_click()  # 增加文章访问量

    # 检测上一篇 下一篇文章
    try:
        pa = Article.objects.get(pk=int(id) - 1)  # 前一篇日志
        if pa.article_type != '2':
            pa = None
    except Exception as e:
        pa = None

    try:
        na = Article.objects.get(pk=int(id) + 1)  # 下篇日志
        if na.article_type != '2':
            na = None
    except Exception as e:
        na = None

    # 已经使用Django上下文来处理以下三个数据
    # userinfo = UserProfile.objects.get(pk=1)#站长资料
    # categorys = Category.objects.all()#获取所有分类
    # siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    tags = article.article_tag.split()  # 获得日志的tag

    if article.article_type != '2':
        return render(request, '404.html')
    else:
        return render(request, 'blog/blog.html', {
            'article': article,
            'pa': pa,
            'na': na,
            # 'userinfo':userinfo,
            # 'siteinfo':siteinfo,
            # 'categorys':categorys,
            'tags': tags, })


def page_not_found(request):
    return render(request, '404.html')


def page_error(request):
    return render(request, '500.html')


def permission_denied(request):
    return render(request, '403.html')


def test(request):
    values = request.META.items()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))


# robots
def robots(request):
    return HttpResponse('User-agent: *')


# sitemap 文件生成
def sitemap(request):
    articles = Article.objects.filter(article_type='2').order_by('-article_create_time')
    return render(request, 'sitemap.html', {'articles': articles}, content_type="text/xml")
