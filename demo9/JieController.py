# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import json
from django.http import HttpResponse
from django.shortcuts import render
from models import Article,User
from django.views.decorators.csrf import csrf_exempt
def view(request):
    status = request.GET.get("status")
    type = request.GET.get("type")
    sort = request.GET.get("sort")
    star = request.GET.get("star")
    context = {}
    if status:
        context['status'] = status
    if type:
        context['type'] = type
    if sort:
        context['sort'] = sort
    if sort:
        context['star'] = star
    sortType = None
    if sort == None or sort == 1:
        sortType = 'comment'
    elif sort == 2:
        sortType = 'createTime'
    page = 12

    # 登录信息
    if request.session.get("user_id"):
        context['login'] = True
        context['title'] = request.session.get("user_title")
        context['headSrc'] = request.session.get("user_head")
        context['username'] = request.session.get("user_name")
        context['level'] = request.session.get("user_level")
    else:
        if "username" in request.COOKIES:
            username = request.COOKIES["username"]
            if username:
                context['username'] = username
                value = User.objects.get(name=username)
                if value:
                    context['login'] = True
                    context['title'] = value.title
                    context['headSrc'] = value.head
                    request.session['user_name'] = value.name
                    request.session['user_id'] = value.id
                    request.session['user_head'] = value.head
                    request.session['user_title'] = value.title
                    request.session['user_level'] = value.level

    # 内容 列表
    article_list = None
    if type:
        if status:
            article_list = Article.objects.filter(type=type, status=status).order_by(sortType)[:page]
        elif star:
            article_list = Article.objects.filter(type=type, star=star).order_by(sortType)[:page]
        else:
            article_list = Article.objects.filter(type=type).order_by(sortType)[:page]
    else:
        if status:
            article_list = Article.objects.filter(status=status).order_by(sortType)[:page]
        elif star:
            article_list = Article.objects.filter(star=star).order_by(sortType)[:page]
        else:
            article_list = Article.objects.order_by(sortType)[:page]

    if article_list:
        context['article_list'] = article_list

    return render(request, 'html/jie/index.html', context)