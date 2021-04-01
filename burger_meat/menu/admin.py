from django.contrib import admin
from .models import *

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('category','name','price',)
    list_filter = ('category','published')


admin.site.register(CategoryMenu)
admin.site.register(Ingridients)