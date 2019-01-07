#coding=utf-8
from random import shuffle
import datetime

from django.conf import settings as original_settings

from blog.models import UserProfile, Siteinfo, Category, Article #导入站长及站长资料model

def site_info(request):
    '''站长资料、网站资料,所有分类上下文'''
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    categorys = Category.objects.all().order_by('category_sort_id')#获取所有分类



    hot_articles = Article.objects.all().order_by('-article_click')[:10]#获取热门文章
    ac_count = Article.objects.count()#获得文章数量
    d1 = datetime.datetime.now()
    d2 = datetime.datetime(2020, 4, 20)
    killpy2 = (d2 - d1).days
    acs= Article.objects.all()
    ac_click = 0
    for ac in acs:
        ac_click += int(ac.article_click)



    # datetimes() 方法返回一个 python 的 datetimes 对象列表
    # 对应着每篇文章的发表时间
    # month 表示精确到月份，DESC 表示降序排列
    dates =  Article.objects.datetimes('article_create_time', 'month', order='DESC')

    
    # 获取文章标签
    l = Article.objects.values("article_tag").distinct().filter(article_type='2')
    tags = []
    for k in l:
        templist = k['article_tag'].split(' ')
        # print(templist)
        for item in templist:
            if item not in tags:
                tags.append(item)
    shuffle(tags)

    tagcss =['am-radius','am-badge-primary','am-badge-secondary','am-badge-success','am-badge-warning','am-badge-danger']
    return {'userinfo':userinfo, 'siteinfo':siteinfo, 'categorys':categorys, 
            'dates':dates, 'alltags':tags, 'tagcss':tagcss,
            'hot_articles':hot_articles,'ac_count':ac_count,'killpy2':killpy2,'ac_click':ac_click,}
'''
这里遇到了一个小小坑，当上下文管理器中定义并返回了一个变量，如果他程序中的视图中的变量重名，那么变量值就会变成视图中的值。
所以这里的tags需要改一个名字。
'''

