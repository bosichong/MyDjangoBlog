#coding=utf-8
from django.contrib import admin

from  .models import UserProfile, Article, Category


class UserProfileAdmin(admin.ModelAdmin):
    """用来显示用户相关"""
    list_display = ('username','email',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Category,CategoryAdmin)