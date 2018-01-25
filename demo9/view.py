# -*- coding:utf-8 -*-
from django.shortcuts import render
from models import User

def hello(request):

    context = {}
    try:
        # 登录信息
        username = request.COOKIES["username"]
        if username:
            context['username'] = username
            value = User.objects.get(name=username)
            if value:
                context['login'] = True
                if value.title:
                    context['title'] = value.title
                if value.head:
                    context['headSrc'] = value.head
    except Exception,e:
        print e.message
    finally:
        print "index ok"

    return render(request, 'html/index.html', context)