from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    category = CategoryMenu.objects.all()
    menu = Menu.objects.filter(published=True)
    context = {'menu':menu,'category':category}
    return render(request,'menu/index.html',context)
