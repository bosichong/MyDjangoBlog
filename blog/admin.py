#coding=utf-8
from django.contrib import admin

from  .models import UserProfile, Article, Category


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

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Article,ArticleAdmin)