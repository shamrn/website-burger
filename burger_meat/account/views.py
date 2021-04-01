from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm,DivErrorList
from .models import Profile

@login_required
def profile(request):
    return render(request,'account/profile.html',{'section':'profile'})


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