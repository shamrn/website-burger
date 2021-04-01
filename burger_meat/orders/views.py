from django.shortcuts import render,redirect
from cart.cart import Cart
from .models import Order,OrderItem
from .forms import OrderCreateForm
from django.urls import reverse
from account.models import Profile

def order_create(request):
    cart = Cart(request)
    if len(cart) == 0:
        return redirect(reverse('menu'))
    else:
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                if request.user.is_authenticated:
                    profile = Profile.objects.get(user=request.user)
                    order = form.save(commit=False)
                    order.user = profile
                    order.save()
                else:
                    order = form.save()
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'])
                request.session['order_id'] = order.id
                cart.clear()
                return redirect(reverse('orders:to_complete'))
        else:
            form = OrderCreateForm()
    return render(request,'orders/order.html',{'cart':cart,'form':form})


def to_complete(request):
    return render(request,'orders/order_to_complete.html')