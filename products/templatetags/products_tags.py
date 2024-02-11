from products.models import Category
from django import template

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Category.objects.all()
