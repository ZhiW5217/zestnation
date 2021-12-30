#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@File  : context_processors
@Author: different && 道阻且长,行则将至 行而不辍,未来可期
@Date  : 2021/12/27
@Desc  : 

"""
from news.models import NewsTypeModels
from brands.models import BrandsModels


def title_types(request):
    new_types = NewsTypeModels.objects.all()
    brand_types = BrandsModels.objects.all()
    return {"new_types": new_types, "brand_types": brand_types}
