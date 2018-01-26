# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import json
from django.http import HttpResponse
from django.shortcuts import render
from models import Article,User
from django.views.decorators.csrf import csrf_exempt
import prpcrypt

@csrf_exempt
def addArticle(request):
    resp = {'status': 1, 'action': '/'}
    prp=prpcrypt.prp()
    try:
        authorName =""
        authorId = 0
        authorHead = ""
        if request.session.get("user_id"):
            authorName = request.session.get("user_name")
            authorId = request.session.get("user_id")
            authorHead = request.session.get("user_head")
        if "username" in request.COOKIES:
            username = request.COOKIES["username"]
            if username:
                name = prp.decrypt(username)
                value = User.objects.get(name=name)
                if value:
                    authorName = value.name
                    authorId = value.id
                    authorHead = value.head
                    request.session['user_name'] = value.name
                    request.session['user_id'] = value.id
                    request.session['user_head'] = value.head
                    request.session['user_title'] = value.title

        else:
            return HttpResponse(json.dumps(resp), content_type="application/json")

        type = request.POST.get("class") # 类型
        title = request.POST.get("title")  # 标题
        content = request.POST.get("content")  # 内容
        experience = request.POST.get("experience")  # 奖励
        article = Article(name=title,content=content,arthorType=type,experience=experience,authorName=authorName,authorId=authorId,authorHead=authorHead)
        article.save()
        resp = {'status': 0, 'action': '/'}
        response = HttpResponse(json.dumps(resp), content_type="application/json")
        return response
    except Exception as e:
        print(e.message)

    return HttpResponse(json.dumps(resp), content_type="application/json")


def view(request):
    context = {}
    # 登录信息
    if "username" in request.COOKIES:
        username = request.COOKIES["username"]
        if username:
            name = prpcrypt.decrypt(username)
            context['username'] = name
            value = User.objects.get(name=name)
            if value:
                context['login'] = True
                if value.title:
                    context['title'] = value.title
                if value.head:
                    context['headSrc'] = value.head
    return render(request, 'html/jie/add.html', context)