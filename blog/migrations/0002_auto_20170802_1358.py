# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章表', 'verbose_name_plural': '文章表'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='birday',
            new_name='user_birday',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='mobile',
            new_name='user_mobile',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='nick_name',
            new_name='user_nick_name',
        ),
        migrations.RemoveField(
            model_name='article',
            name='synopsis',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='sort_id',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='image',
        ),
        migrations.AddField(
            model_name='article',
            name='article_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='所属分类'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_click',
            field=models.IntegerField(default=0, verbose_name='文章点击量'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_content',
            field=models.TextField(default='', verbose_name='博客正文'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='image/article/default.png', upload_to='image/article/%Y/%m', verbose_name='文章配图'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_support',
            field=models.CharField(choices=[('1', '推荐'), ('0', '取消推荐')], default='0', max_length=10, verbose_name='文章推荐'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_synopsis',
            field=models.TextField(default='', verbose_name='日志简介'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_title',
            field=models.CharField(default='', max_length=50, verbose_name='日志标题'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_type',
            field=models.CharField(choices=[('0', '草稿'), ('1', '软删除'), ('2', '正文')], default='0', max_length=10, verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_up',
            field=models.CharField(choices=[('1', '置顶'), ('0', '取消置顶')], default='0', max_length=10, verbose_name='文章置顶'),
        ),
        migrations.AddField(
            model_name='article',
            name='article_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='文章作者'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_detail',
            field=models.CharField(default='', max_length=100, verbose_name='分类介绍'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_name',
            field=models.CharField(default='', max_length=20, verbose_name='分类名称'),
        ),
        migrations.AddField(
            model_name='category',
            name='category_sort_id',
            field=models.IntegerField(default=1, verbose_name='分类排序'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_address',
            field=models.CharField(default='', max_length=200, verbose_name='用户地址'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_gender',
            field=models.CharField(choices=[('1', '男'), ('0', '女')], default='1', max_length=10, verbose_name='性别选择'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='user_image',
            field=models.ImageField(default='image/user/default.png', upload_to='image/user/%Y/%m', verbose_name='用户头像'),
        ),
    ]
