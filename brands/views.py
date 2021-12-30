from django.shortcuts import render

# Create your views here.
from brands.models import BrandsModels


def brands(request, pk):
    # todo 排版问题
    # 获取品牌相关的所有产品
    brand = BrandsModels.objects.filter(pk=pk).first()
    # 集合排版的产品
    products = brand.product.filter(status=True, product_typesetting=False).all()

    # 单屏排版的产品
    products_up = brand.product.filter(status=True, product_typesetting=True, product_top=True).order_by(
        '-update_time').all()
    products_down = brand.product.filter(status=True, product_typesetting=True, product_top=False).order_by(
        '-update_time').all()

    return render(request, 'brand.html', locals())
