from django.contrib import admin
from .models import Shares

@admin.register(Shares)
class SharesAdmin(admin.ModelAdmin):
    list_display = ['body','status']
    list_filter = ('status',)
