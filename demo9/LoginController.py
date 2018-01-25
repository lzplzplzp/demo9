# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse
from django.shortcuts import render
from models import User

def login(request):

    try:
        phone = request.POST.get("phone")
        password = request.POST.get("pass")
        User.objects.get(name="WeizhongTu",password=password)

        resp = {'errorcode': 100, 'detail': 'Get success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    except Exception,e:
        print e.message
    finally:
        print "ok"


def view(request):
    return render(request, 'html/user/login.html')