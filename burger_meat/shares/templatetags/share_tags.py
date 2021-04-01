from django import template
from ..models import Shares



register = template.Library()


@register.simple_tag
def show_shares():
    return Shares.objects.filter(status='published')

# @register.inclusion_tag('shares/share.html')
# def show_shares():
#     shares = Shares.objects.filter(status='published')
#     return {'shares':shares}