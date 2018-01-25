# -*- coding:utf-8 -*-
import json
import sqlite3
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection, transaction
from models import User


@csrf_exempt
def reg(request):

    resp = {'status': 0, 'action': '/'}
    try:
        phone= request.POST.get("phone")
        username=request.POST.get("username")
        password=request.POST.get("pass")

        user = User(name=username, phone=phone, password=password)
        user.save()
        response = HttpResponse(json.dumps(resp), content_type="application/json")
        response.set_cookie("username", username, 3600)
        return response
    except Exception,e:
        print e.message
        resp = {'status': 1}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    finally:
        print "ok"





def view(request):
    return render(request, 'html/user/reg.html')