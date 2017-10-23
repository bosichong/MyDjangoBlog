#coding=utf-8
from django.contrib import admin
from django.utils.safestring import mark_safe

from  .models import UserProfile, Article, Category, Siteinfo, Acimage




class UserProfileAdmin(admin.ModelAdmin):
    """用来显示用户相关"""
    #用来显示用户字段
    list_display = ('username','user_nick_name','email','user_gender','user_mobile','user_address')
    #过滤器设置
    list_filter = ('username','user_nick_name','email')
    #搜索
    search_fields = ('username','user_nick_name','email')
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','category_detail','category_sort_id')
    #过滤器设置
    list_filter = ('category_name','category_sort_id')


class ArticleAdmin(admin.ModelAdmin):
    """文章字段"""
    list_display = ('article_title','article_user','article_category','article_type','article_up','article_support','article_click')

    #list_per_page设置每页显示多少条记录，默认是100条
    list_per_page = 15
    #筛选器
    list_filter = ('article_category', 'article_create_time') #过滤器
    search_fields = ('article_title', )          #搜索字段
    date_hierarchy = 'article_create_time'        #详细时间分层筛选

class SiteinfoAdmin(admin.ModelAdmin):
    list_display = ('site_name','site_user','site_detail')



class AcimageAdmin(admin.ModelAdmin):
    list_display = ('image_title', 'image_detail', 'image_url', 'image_data')
    readonly_fields = ('image_data', 'image_url',)  #必须加这行 否则访问编辑页面会报错
    def image_url(self, obj):
        return mark_safe(u'<a href="%s">右键复制图片地址</a>' % obj.image_path.url)

    def image_data(self, obj):
        img = mark_safe(u'<img src="%s" width="100px" />' % obj.image_path.url)
        return img
    # 页面显示的字段名称
    image_data.short_description = u'图片'
    image_url.short_description = u'图片地址'

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Siteinfo,SiteinfoAdmin)
admin.site.register(Acimage,AcimageAdmin)