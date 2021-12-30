#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@File  : views
@Author: different && 道阻且长,行则将至 行而不辍,未来可期
@Date  : 2021/12/16
@Desc  : 

"""
from django.shortcuts import render

from brands.models import BrandsModels
from news.models import NewsModels


def index(request):
    news = NewsModels.objects.filter(show=True).order_by('-update_time')[:3]
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')
