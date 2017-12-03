from django import template

register = template.Library()


@register.filter(name='colum_for_items')
def colum_for_items(value):
    """calculate column size for display N items"""
    return int(12 / value)


