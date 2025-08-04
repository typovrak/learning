from django import template
from django.template import Node

register = template.Library()


@register.simple_tag
def hello(name):
    return f"Hello, {name}!"


@register.filter
def upperfirst(value):
    return value[0].upper() + value[1:]


class UpperNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        content = self.nodelist.render(context)
        return content.upper()


@register.tag(name="upper")
def do_upper(parser, token):
    nodelist = parser.parse(("endupper",))
    parser.delete_first_token()
    return UpperNode(nodelist)
