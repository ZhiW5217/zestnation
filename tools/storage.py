#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

"""
@File  : storage
@Author: different && 道阻且长,行则将至 行而不辍,未来可期
@Date  : 2021/12/23
@Desc  : 图片上传重写

"""

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.conf import settings
import os, time, random


class ImageStorage(FileSystemStorage):
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    def _save(self, name, content):
        # 扩展名
        ext = os.path.splitext(name)[1]

        # 文件目录
        d = os.path.dirname(name)

        # 定义文件名
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)

        # 重写合成文件名
        name = os.path.join(d, fn + ext)
        return super(ImageStorage, self)._save(name, content)
