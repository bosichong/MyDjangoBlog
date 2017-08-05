#coding=utf-8
import xadmin


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class UserProfileAdmin(object):
    list_display = ['name','user_nick_name']



xadmin.site.register(UserProfile, UserProfileAdmin)