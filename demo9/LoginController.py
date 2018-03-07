# -*- coding:utf-8 -*-
from __future__ import print_function
from __future__ import print_function
import json
from django.http import HttpResponse
from django.shortcuts import render
from models import User
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    resp = {'status': 1, 'action': '/'}
    try:
        phone = request.POST.get("phone")
        password = request.POST.get("pass")
        value = User.objects.get(phone=phone)
        if value:
            request.session['user_name'] = value.name
            request.session['user_id'] = value.id
            request.session['user_head'] = value.head
            request.session['user_title'] = value.title
            request.session['user_level'] = value.level
            if value.password==password:
                resp = {'status': 0, 'action': '/'}
                response = HttpResponse(json.dumps(resp), content_type="application/json")
                response.set_cookie("username", value.name, 3600)
                return response
    except Exception as e:
        print(e.message)

    return HttpResponse(json.dumps(resp), content_type="application/json")


def view(request):
    return render(request, 'html/user/login.html')