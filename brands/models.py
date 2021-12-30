from django.db import models

# Create your models here.
from tools import status_choices
from tools.storage import ImageStorage

"""
品牌ID
产品ID
序号
背景图
超链接
小产品图
产品名称
产品型号
"""


class BrandsModels(models.Model):
    brand_name = models.CharField(max_length=255, verbose_name="品牌名称")
    brand_logo = models.ImageField(blank=True, null=True, upload_to="images/brands/brands_logo/%Y%m%d",
                                   storage=ImageStorage,
                                   verbose_name="品牌logo(80x20)")
    brand_images = models.ImageField(upload_to="images/brands/brands_images/%Y%m%d", storage=ImageStorage,
                                     verbose_name="品牌背景图片(1920x950)",
                                     blank=True, null=True)
    brand_images_m = models.ImageField(upload_to="images/brands/brands_images/%Y%m%d", storage=ImageStorage,
                                       verbose_name="手机端品牌图片(750x1334)", blank=True, null=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间', blank=True, null=True)

    def __str__(self):
        return self.brand_name

    class Meta:
        db_table = 't_brands'
        verbose_name = '品牌'
        verbose_name_plural = '品牌'


class ProductModels(models.Model):
    product_name = models.CharField(max_length=255, verbose_name="产品名称")
    product_type = models.CharField(max_length=50, verbose_name="产品型号", null=True, blank=True)
    status = models.BooleanField(default=False, choices=status_choices('草稿', '发布'), verbose_name="页面状态", null=True,
                                 blank=True)
    product_typesetting = models.BooleanField(default=False, choices=status_choices('集合页面排版', '独立页面排版'),
                                              verbose_name="页面排版", null=True, blank=True)
    product_top = models.BooleanField(default=False, choices=status_choices('非置顶', '置顶'), verbose_name="排版置顶",
                                      blank=True, null=True)
    brand = models.ForeignKey(to=BrandsModels, on_delete=models.CASCADE, blank=True, null=True, related_name='product',
                              verbose_name="品牌")
    product_first_image = models.ImageField(upload_to="images/brands/first_image/%Y%m%d", storage=ImageStorage,
                                            verbose_name="产品首图(透明180x180)", blank=True, null=True)
    product_first_image_m = models.ImageField(upload_to="images/brands/first_image_m/%Y%m%d", storage=ImageStorage,
                                              verbose_name="手机端产品首图(透明100x100)", blank=True, null=True)
    product_background_image = models.ImageField(upload_to="images/brands/background_image/%Y%m%d",
                                                 storage=ImageStorage,
                                                 verbose_name="产品背景图(1920x950)", blank=True,
                                                 null=True)
    product_background_image_m = models.ImageField(upload_to="images/brands/background_image_m/%Y%m%d",
                                                   storage=ImageStorage,
                                                   verbose_name="手机端产品背景图(750x1334)", blank=True,
                                                   null=True)

    product_url = models.CharField(max_length=255, verbose_name="产品链接", null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间', blank=True, null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        db_table = 't_product'
        verbose_name = '产品'
        verbose_name_plural = '产品'
