#coding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser

#创建字段的时候要么设置可以为空，要么就需要设置默认值。

class UserProfile(AbstractUser):
    """继承django系统自带的user创建用户表，
        1.配置文件中要添加 AUTH_USER_MODEL = "blog.UserProfile"
        2.引入from django.contrib.auth.models import AbstractUser
        3.admin.py 中注册用户表 admin.site.register(UserProfile)
        4. 如果之前先生成了数据库表，之后修改的user要重新生成表，最好先清空数据库。
    """
    user_nick_name = models.CharField(max_length=24, verbose_name=u'用户昵称', default="")
    user_gender = models.CharField(max_length=10, choices=(("1",u"男"),("0","女")), default="1", verbose_name=u"性别选择")
    user_birday = models.DateField(verbose_name=u"用户生日", null=True, blank=True)
    user_mobile = models.CharField(max_length=11, null=True, blank=True)
    user_address = models.CharField(max_length=200, verbose_name=u"用户地址", default='')
    #需要安装 pip install Pillow
    user_image = models.ImageField(upload_to="image/user/%Y/%m", default="image/user/default.png", max_length=100, verbose_name=u"用户头像")

    class Meta:
        verbose_name=u'用户表'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.username



class Category(models.Model):
    """blog 分类"""
    category_name = models.CharField(max_length=20, verbose_name=u'分类名称', default='')
    category_detail = models.CharField(max_length=100, verbose_name=u'分类介绍', default='')
    category_sort_id = models.IntegerField(verbose_name=u'分类排序', default=1)

    class Meta:
        verbose_name = u'博客分类'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.name


class Article(models.Model):
    """博客文章"""
    article_title = models.CharField(max_length=50, verbose_name=u'日志标题', default='')
    article_synopsis = models.TextField(verbose_name=u'日志简介', default='')
    article_image = models.ImageField(upload_to="image/article/%Y/%m", default="image/article/default.png", max_length=100, verbose_name=u"文章配图")
    article_user = models.ForeignKey(UserProfile, verbose_name=u'文章作者', null=True, blank=True)
    article_category = models.ForeignKey(Category, verbose_name=u'所属分类', null=True, blank=True)
    article_content = models.TextField(verbose_name=u'博客正文', default='')
    article_type = models.CharField(max_length=10, choices=(("0",u"草稿"),("1","软删除"),("2","正文")), default="0", verbose_name=u"文章类别")
    article_click = models.IntegerField(verbose_name=u'文章点击量', default=0)
    article_up = models.CharField(max_length=10, choices=(("1",u"置顶"),("0","取消置顶")), default="0", verbose_name=u"文章置顶")
    article_support= models.CharField(max_length=10, choices=(("1",u"推荐"),("0","取消推荐")), default="0", verbose_name=u"文章推荐")
        
    class Meta:
        verbose_name=u'文章表'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.article_title