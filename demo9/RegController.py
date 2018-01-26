# -*- coding:utf-8 -*-
import json
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse
from models import User
import prpcrypt


@csrf_exempt
def reg(request):
    prp = prpcrypt.prp()
    resp = {'status': 0, 'action': '/'}
    phone= request.POST.get("phone")
    username=request.POST.get("username")
    password=request.POST.get("pass")
    user = User(name=username, phone=phone, password=password)
    user.save()
    response = HttpResponse(json.dumps(resp), content_type="application/json")
    response.set_cookie("username", prp.encrypt(username) , 3600)
    request.session['user_name'] = user.name
    request.session['user_id'] = user.id
    request.session['user_head'] = user.head
    request.session['user_title'] = user.title
    request.session['user_level'] = user.level
    return response

def view(request):
    return render(request, 'html/user/reg.html')