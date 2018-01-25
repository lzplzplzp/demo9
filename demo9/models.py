# -*- coding: utf-8 -*-

from django.db import models

class Article(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=5000)
    authorName = models.CharField(max_length=30)
    authorId = models.IntegerField()
    authorHead = models.CharField(max_length=30)
    arthorType = models.IntegerField()
    createTime = models.DateField(auto_now_add=True)
    modifyTime = models.DateField(auto_now=True)

class User(models.Model):
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    head = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    level = models.IntegerField()

