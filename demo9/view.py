# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.db import connection, transaction

def hello(request):
    cursor = connection.cursor()
    context={}
    try:
        context['hello']="oshifohf,,,asa"
        username = request.COOKIES["username"]
        if username:
            context['username'] = username
            cursor.execute('select title,headSrc from user WHERE name='+username)
            values = cursor.fetchall()
            if values:
                context['login'] = True
                if values[0][0]:
                    context['title']=values[0][0]
                if values[0][1]:
                    context['headSrc'] = values[0][1]

    except Exception,e:
        print e.message
    finally:
        cursor.close()

    return render(request,'html/index.html',context)