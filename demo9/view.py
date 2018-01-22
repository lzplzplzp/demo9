from django.http import HttpResponse
from django.shortcuts import render
import redisC

def hello(request):
    context={}
    context['hello']="oshifohf,,,asa"
    context['name']=redisC.rcon().get('name')
    return render(request,'hello.html',context)