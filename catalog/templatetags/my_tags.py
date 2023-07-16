from django import template
import datetime
register = template.Library()

@register.simple_tag()
def mediapath(data) -> str:
    if data:
        return f"/media/{data}"


@register.filter
def mediapath(value):
    if value:
        return f"/media/{value}"
