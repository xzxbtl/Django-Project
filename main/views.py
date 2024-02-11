from django.shortcuts import render
from products.models import Category


def index(request):
    content = {
        'title': 'Home - Main',
        'content': 'Furniture Shop Home',
    }
    return render(request, 'main/index.html', content)


def about(request):
    content = {
        'title': 'Home - About us',
        'content': 'About us',
        'text_on_page': 'We have been operating since 2004, we have more than 100 thousand customers and about 34 '
                        'stores across the country! you can view the reviews of our products if in doubt'
    }
    return render(request, 'main/about.html', content)