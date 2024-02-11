from django.shortcuts import render
from products.models import Products


def catalog(request):
    products = Products.objects.all()

    context = {
        'title': 'Home - Catalog',
        'products': products
    }
    return render(request, 'products/catalog.html', context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)
