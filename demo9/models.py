# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=5000)
    authorName = models.CharField(max_length=30)
    authorId = models.IntegerField()
    authorHead = models.CharField(max_length=30)
    arthorType = models.IntegerField()
    # 0 提问1 分享2 讨论3 建议 4 公告 5 动态
    type = models.IntegerField()
    # 状态 0 未结  1 已结
    status = models.IntegerField()
    # 经验
    experience = models.IntegerField()
    # 评论数
    comment = models.IntegerField()
    createTime = models.DateField(auto_now_add=True)
    modifyTime = models.DateField(auto_now=True)
    # 0 普通  1 精华 2 置顶
    star = models.IntegerField()


class User(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    head = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    level = models.IntegerField()



