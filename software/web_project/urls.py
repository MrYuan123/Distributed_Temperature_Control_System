#coding=utf-8
from django.conf.urls import url, include

from web_project import admin
from . import views

urlpatterns = [
    url(r'^$',views.sayHello),
    url(r'^blank/$',views.blank),
    url(r'^tables/$',views.tables),
    url(r'^flot/$',views.flot),
    url(r'^AjaxTable/$', views.AjaxTable),
    url(r'^data/$',views.renew),
]