from django.contrib import admin
from .models import Order,OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','status_order','created']
    list_display_links = ('id','status_order','created',)
    inlines = [OrderItemInline]