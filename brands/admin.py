import time
from datetime import datetime

from django.contrib import admin

# Register your models here.
from brands.models import ProductModels, BrandsModels
from zestnation import settings
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(BrandsModels)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ['brand_name', 'create_time']


@admin.register(ProductModels)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'product_type', 'brand', 'product_typesetting', 'product_top', 'status',
                    'create_time', 'update_time']

    # 分页
    list_per_page = settings.LIST_PER_PAGE
    # 排序方式
    ordering = ['create_time']
    # 允许搜索的字段
    search_fields = ['title']
    # 显示详细时间
    date_hierarchy = 'create_time'

    # 过滤器
    list_filter = ['brand', 'create_time']

    @admin.action(description="置顶/取消置顶")
    def product_top(self, request, queryset):
        if queryset.first().product_top:
            updated = queryset.update(product_top=False)
        else:
            updated = queryset.update(product_top=True)

        queryset.update(update_time=datetime.now())
        self.message_user(request, ngettext(
            '%d 个页面修改成功。',
            '%d 个页面修改成功。',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description="发布/草稿")
    def make_status(self, request, queryset):
        if queryset.first().status:
            updated = queryset.update(status=False)
        else:
            updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d 个产品状态修改成功。',
            '%d 个产品状态修改成功。',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='修改排版')
    def make_typesetting(self, request, queryset):
        if queryset.first().product_typesetting:
            updated = queryset.update(product_typesetting=False)
        else:
            updated = queryset.update(product_typesetting=True)
        self.message_user(request, ngettext(
            '%d 个文章排版状态修改成功。',
            '%d 个文章排版状态修改成功。',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [make_status, make_typesetting, product_top]

    admin.site.site_title = '沁泽通达官网后台管理'
    admin.site.site_header = '沁泽通达官网后台管理'
