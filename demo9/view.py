# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import User,Article
import prpcrypt

def hello(request):
    status = request.GET.get("status")
    type = request.GET.get("type")
    sort = request.GET.get("sort")
    sortType = None
    if sort == None or sort == 1:
        sortType = 'comment'
    elif sort == 2:
        sortType = 'createTime'
    page = 12
    context = {}
    prp=prpcrypt.prp()
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
                name=prp.decrypt(username)
                context['username'] = name
                value = User.objects.get(name=name)
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
    article_list1=Article.objects.filter(status=2)[:5]
    if article_list1:
        context['article_list1'] = article_list1
    # 内容 列表
    article_list2= None
    if type:
        article_list2= Article.objects.filter(type=type).exclude(type=2)[:page]
    elif status:
        article_list2 = Article.objects.filter(status=status).exclude(type=2)[:page]
    else:
        article_list2 = Article.objects.exclude(status=2).order_by(sortType)[:page]
    if article_list2:
        context['article_list2'] = article_list2


    return render(request, 'html/index.html', context)


def header(request):
    context = {}
    prp = prpcrypt.prp()
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
                name = prp.decrypt(username)
                context['username'] = name
                value = User.objects.get(name=name)
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