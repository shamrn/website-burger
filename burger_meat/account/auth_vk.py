
from .models import Profile

def auth_vk(vk_id):
    if str(vk_id)[0:2] == 'id':
        if not Profile.objects.filter(user=vk_id).exists():
            Profile.objects.create(user=vk_id)