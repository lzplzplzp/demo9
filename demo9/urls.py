"""demo9 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# from django.conf.urls import include, url
# from django.contrib import admin

from django.conf.urls import url
from django.conf.urls.static import static
from . import view
from . import LoginController
from . import RegController
from . import ArticleController
from . import settings

urlpatterns = [
    url(r'^header$', view.header),
    url(r'^$', view.hello),
    url(r'^user/login$', LoginController.view),
    url(r'^login$', LoginController.login),
    url(r'^reg$', RegController.reg),
    url(r'^user/reg$', RegController.view),
    url(r'^jie/add$', ArticleController.view),
    url(r'^addArticle$', ArticleController.addArticle),

]+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
