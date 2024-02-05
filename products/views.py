from django.shortcuts import render


def catalog(request):
    return render(request, 'products/catalog.html')


def product(request):
    return render(request, 'products/product.html')