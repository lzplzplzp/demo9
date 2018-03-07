# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import User,Article

def hello(request):
    context = {}
    status = request.GET.get("status")
    type = request.GET.get("type")
    star = request.GET.get("star")
    sort = request.GET.get("sort")
    if status:
        context['status'] = status
    if type:
        context['type'] = type
    if star:
        context['star'] = star
    if sort:
        context['sort'] = sort
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

    # 内容 置顶
    article_list1=Article.objects.filter(star=2)[:5]
    if article_list1:
        context['article_list1'] = article_list1
    # 内容 列表
    article_list2= None
    if type:
        article_list2= Article.objects.filter(type=type).exclude(star=2)[:page]
    elif status:
        article_list2 = Article.objects.filter(status=status).exclude(star=2)[:page]
    elif star:
        article_list2 = Article.objects.filter(star=1)[:page]
    else:
        article_list2 = Article.objects.exclude(star=2).order_by(sortType)[:page]
    if article_list2:
        context['article_list2'] = article_list2


    return render(request, 'html/index.html', context)


def header(request):
    context = {}

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

    return render(request, 'html/common/header.html', context)