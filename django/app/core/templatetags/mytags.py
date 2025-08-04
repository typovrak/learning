from django import template

register = template.Library()


@register.simple_tag
def hello(name):
    return f"Hello, {name}!"


@register.filter
def upperfirst(value):
    return value[0].upper() + value[1:]
