from django.shortcuts import render


def index(request):
    context = {
        'title': 'GeekStore'
    }
    return render(request, 'mainapp/index.html')


def products(request):
    context = {
        'title': 'Каталог',
        'items': [
            {
                'id': 1,
                'title': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'img': 'Adidas-hoodie.png',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'id': 2,
                'title': 'Синяя куртка The North Face',
                'price': 23725,
                'img': 'Adidas-hoodie.png',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'id': 3,
                'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390,
                'img': 'Adidas-hoodie.png',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'
            },
            {
                'id': 4,
                'title': 'Черный рюкзак Nike Heritage',
                'price': 2340,
                'img': 'Adidas-hoodie.png',
                'description': 'Плотная ткань. Легкий материал.'
            },
            {
                'id': 5,
                'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': 13590,
                'img': 'Adidas-hoodie.png',
                'description': 'Гладкий кожаный верх. Натуральный материал.'
            },
            {
                'id': 6,
                'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': 2890,
                'img': 'Adidas-hoodie.png',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.'
            },
        ]
    }
    return render(request, 'mainapp/products.html', context)
