#coding=utf-8
from django.conf import settings as original_settings

from blog.models import UserProfile, Siteinfo, Category #导入站长及站长资料model

def site_info(request):
    '''站长资料、网站资料,所有分类上下文'''
    userinfo = UserProfile.objects.get(pk=1)#站长资料
    siteinfo = Siteinfo.objects.get(pk=1)#获取站点信息
    categorys = Category.objects.all().order_by('category_sort_id')#获取所有分类
    return {'userinfo':userinfo, 'siteinfo':siteinfo, 'categorys':categorys}


