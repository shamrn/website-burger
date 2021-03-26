from django.shortcuts import render
from .models import *
from django.views.generic import ListView
from cart.forms import CartAddProductForm

class MenuListView(ListView):
    queryset = Menu.objects.filter(published=True)
    context_object_name = 'menu'
    template_name = 'menu/menu.html'

    def get_context_data(self,*,object_list=None,**kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm()
        return context
