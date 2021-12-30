#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@File  : urls
@Author: different && 道阻且长,行则将至 行而不辍,未来可期
@Date  : 2021/12/21
@Desc  : 

"""
from django.urls import path

from news import views

urlpatterns = [
    path('news/<pk>', views.news, name='news'),
    path('news/art/<pk>', views.arts, name='arts')
]
