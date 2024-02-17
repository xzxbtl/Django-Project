from django.utils.http import urlencode

from products.models import Category
from django import template

register = template.Library()


@register.simple_tag()
def tag_categories():
    return Category.objects.all()


@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)

