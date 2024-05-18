from django import template

register = template.Library()


@register.filter
def strip_trailing_zeros(value):
    try:
        value = float(value)
        return ("%f" % value).rstrip("0").rstrip(".")
    except (ValueError, TypeError):
        return value
