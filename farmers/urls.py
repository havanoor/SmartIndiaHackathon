from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.loginUser,name='login'),
    path('register/',views.register,name='newuser'),
    path('home/',views.home,name='home'),
    path('withdraw/<str:value>/',views.withdraw,name="withdraw"),
    path('calc/<str:value>/',views.calculate,name="cash"),
    path('buy/',views.purchase,name='buy'),
    
    
    
]