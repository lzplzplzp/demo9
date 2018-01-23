# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse

def login(request):
    resp = {'errorcode': 100, 'detail': 'Get success'}
    return HttpResponse(json.dumps(resp), content_type="application/json")