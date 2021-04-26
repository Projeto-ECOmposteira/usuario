from django import template
from decouple import config

register = template.Library()

@register.simple_tag
def get_domain_link():
    return config('FRONT_BASE_URL')