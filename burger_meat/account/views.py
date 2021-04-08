from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,DivErrorList,UserEditProfile
from .models import Profile
from orders.models import Order,OrderItem
from .auth_vk import auth_vk

@login_required
def profile(request):
    user = request.user
    auth_vk(user)
    form = UserEditProfile()
    profile = Profile.objects.get(user=user)
    orders = OrderItem.objects.filter(order__user=profile) #Order.objects.filter(user=profile)
    if request.method == 'POST':
        edit_form = UserEditProfile(request.POST)
        if edit_form.is_valid():
            cd = edit_form.cleaned_data
            profile.name,profile.address,profile.phone = cd['name'] , cd['address'], cd['phone']
            profile.save()
    return render(request,'account/profile.html',{'profile':profile,'form':form,'orders':orders})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST,error_class=DivErrorList)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user,email=cd['email'],phone=cd['phone'])
            return render(request,'account/register_done.html',{'new_user':new_user})
    else:
        user_form = UserRegistrationForm(error_class=DivErrorList)
    return render(request,'account/register.html',{'user_form':user_form})
