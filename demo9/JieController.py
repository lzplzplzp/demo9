# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import json
from django.http import HttpResponse
from django.shortcuts import render
from models import Article,User
from django.views.decorators.csrf import csrf_exempt
import prpcrypt
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
    return render(request, 'html/jie/index.html', context)