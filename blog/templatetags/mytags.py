#coding=utf-8

#导入基本配置文件
from django import template

from markdown import markdown
register = template.Library()

#自定义过滤器

@register.filter
def toMarkdown(str):
    """markdown解析器"""
    return markdown(str)