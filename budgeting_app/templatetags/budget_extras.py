from django import template
from urllib.parse import urlencode
from collections import OrderedDict



register = template.Library()

# TODO: Sort transactions by selected heading, reversing the order on second click
@register.simple_tag
def url_replace(data, value, direction=''):
    pass


@register.simple_tag
def as_currency(amount):
    if amount >= 0:
        return '+${:,.2f}'.format(amount)
    else:
        return '-${:,.2f}'.format(-amount)