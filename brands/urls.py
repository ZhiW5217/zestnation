#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@File  : urls
@Author: different && 道阻且长,行则将至 行而不辍,未来可期
@Date  : 2021/12/21
@Desc  : 

"""
from django.urls import path

from brands import views

urlpatterns = [
    path('brand/<pk>', views.brands, name='brands'),
]