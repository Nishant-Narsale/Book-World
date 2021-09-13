from django import template

register = template.Library()

@register.filter
def to_url(value):
    return value[1:]