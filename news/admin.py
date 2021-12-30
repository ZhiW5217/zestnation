from datetime import datetime

from django.contrib import admin

# Register your models here.
from news.models import NewsModels, NewsTypeModels
from zestnation import settings
from django.contrib import messages
from django.utils.translation import ngettext


@admin.register(NewsTypeModels)
class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['type_name']


@admin.register(NewsModels)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['article_title', 'article_type', 'article_author', 'status', 'show','show_time', 'create_time']

    list_per_page = settings.LIST_PER_PAGE

    # 排序方式
    ordering = ['create_time']
    # 允许搜索的字段
    search_fields = ['article_title']
    # 显示详细时间
    date_hierarchy = 'create_time'

    # 过滤器
    list_filter = ['article_type', 'create_time']

    @admin.action(description="发布/草稿")
    def make_status(self, request, queryset):
        if queryset.first().status:
            updated = queryset.update(status=False)
        else:
            updated = queryset.update(status=True)
        self.message_user(request, ngettext(
            '%d 个文章状态修改成功。',
            '%d 个文章状态修改成功。',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description="展示/取消")
    def make_show(self, request, queryset):
        if queryset.first().show:
            updated = queryset.update(show=False)
        else:
            updated = queryset.update(show=True)
        queryset.update(update_time=datetime.now())
        self.message_user(request, ngettext(
            '%d 个文章状态修改成功。',
            '%d 个文章状态修改成功。',
            updated,
        ) % updated, messages.SUCCESS)

    actions = [make_status, make_show]
