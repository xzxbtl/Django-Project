from django.shortcuts import render, get_list_or_404
from products.models import Products
from django.core.paginator import Paginator


def catalog(request, category_slug, page=1):
    if category_slug == 'all':
        products = Products.objects.all()
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))  # Если нету в категории
        # нечего ошибка 404

    paginator = Paginator(products, 3)
    current_page = paginator.page(page)

    context = {
        'title': 'Home - Catalog',
        'products': current_page,
        'slug_url': category_slug
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)
