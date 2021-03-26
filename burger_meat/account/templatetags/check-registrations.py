from django import template
from ..models import Profile

register = template.Library()

@register.inclusion_tag('templates/account/registerras.html',name='check_reg')
def check_registrations(values):
    objects_list = Profile.objects.all()
    print(values)
