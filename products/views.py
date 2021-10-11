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


def test_context(request):
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожловать на сайт!',
        'user': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': True,
    }
    return render(request, 'products/test_context.html', context)
