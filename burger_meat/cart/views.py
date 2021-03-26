from django.shortcuts import render,get_object_or_404,redirect
from .cart import Cart
from django.views.decorators.http import require_POST
from menu.models import Menu
from .forms import CartAddProductForm



@require_POST
def cart_add(request,product_id):
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        product = get_object_or_404(Menu,id=product_id)
        cd = form.cleaned_data
        cart = Cart(request)
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
        if cd['update']:
            return redirect('cart:cart_detail')
    return redirect('menu')

def cart_detail(request):
    cart = Cart(request)

    return render(request,'cart/detail.html',{'cart':cart})

def cart_remove(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Menu,id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')