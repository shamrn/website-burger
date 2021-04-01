from django.urls import path
from .views import *

urlpatterns = [
    path('',MenuListView.as_view(),name='menu'),
]