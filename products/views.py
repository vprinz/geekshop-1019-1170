import os
import json

from django.shortcuts import render

MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {'title': 'GeekShop'}
    return render(request, 'products/index.html', context)


def products(request):
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'GeekShop - Каталог',
        'products': json.load(open(file_path, encoding='utf-8'))
    }
    return render(request, 'products/products.html', context)
