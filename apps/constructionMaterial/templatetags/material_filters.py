# templatetags/material_filters.py

from django import template

register = template.Library()

@register.filter(name='mul')
def mul(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})