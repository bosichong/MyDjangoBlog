#coding=utf-8
from django.conf import settings as original_settings

from blog.models import UserProfile, Siteinfo, Category, Article #导入站长及站长资料model

def site_info(request):
    '''站长资料、网站资料,所有分类上下文'''
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    categorys = Category.objects.all().order_by('category_sort_id')#获取所有分类
    # datetimes() 方法返回一个 python 的 datetimes 对象列表
    # 对应着每篇文章的发表时间
    # month 表示精确到月份，DESC 表示降序排列
    dates =  Article.objects.datetimes('article_create_time', 'month', order='DESC')
    return {'userinfo':userinfo, 'siteinfo':siteinfo, 'categorys':categorys, 'dates':dates,}


