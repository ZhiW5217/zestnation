from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.
from tools import status_choices
from tools.storage import ImageStorage

"""
文章ID
文章类型
新闻标题
创建人
创建时间
展示时间
状态
正文（富文本）
修改日志
"""


class NewsTypeModels(models.Model):
    type_name = models.CharField(max_length=255, verbose_name="新闻类型")

    def __str__(self):
        return self.type_name

    class Meta:
        db_table = 't_article_type'
        verbose_name = '新闻类型'
        verbose_name_plural = '新闻类型'


class NewsModels(models.Model):
    article_title = models.CharField(max_length=255, verbose_name="文章标题")
    article_img = models.ImageField(upload_to="images/news/article_img/%Y%m%d", storage=ImageStorage,
                                    verbose_name="文章首图(435x260)", blank=True, null=True)
    article_info = models.TextField(verbose_name='文章简介', blank=True, null=True)
    article_type = models.ForeignKey(to=NewsTypeModels, on_delete=models.CASCADE, blank=True, null=True,
                                     related_name='new', verbose_name="类型")
    article_author = models.CharField(max_length=50, verbose_name="创建人")
    status = models.BooleanField(default=False, choices=status_choices('草稿', '发布'), verbose_name="文章状态")
    show = models.BooleanField(default=False, choices=status_choices(), verbose_name="首页展示")
    show_time = models.DateField(blank=True, null=True, auto_now=False, verbose_name="展示时间")
    article_desc = RichTextUploadingField(verbose_name="文章内容")
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间', blank=True, null=True)

    def __str__(self):
        return self.article_title

    class Meta:
        db_table = 't_article'
        verbose_name = '新闻'
        verbose_name_plural = '新闻'
