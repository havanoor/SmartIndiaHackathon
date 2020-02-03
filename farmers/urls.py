from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.loginUser,name='login'),
    path('register/',views.register,name='newuser'),
    path('home/',views.home,name='home'),
    
]