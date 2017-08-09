#coding=utf-8

#导入基本配置文件
from django import template

from markdown import markdown

from ..models import Article, Category
register = template.Library()

#自定义过滤器

@register.filter
def toMarkdown(str):
    """markdown解析器"""
    return markdown(str)

@register.filter
def cat_count(cat_id):
    """统计分类下边的日志数"""
    return Article.objects.filter(article_category=cat_id).count()