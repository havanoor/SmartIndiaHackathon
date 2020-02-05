from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #login page of main website
    path('',views.loginUser,name='login'),

    #To create a new user for our website
    path('register/',views.register,name='newuser'),

    #Main homepage of our website
    path('home/',views.home,name='home'),

    #Used to make transactions on the website
    path('withdraw/<str:value>/',views.withdraw,name="withdraw"),
    #
    path('calc/<str:value>/',views.calculate,name="cash"),

    #TO buy new things from the market
    path('buy/',views.purchase,name='buy'),

    #Registering details of new user
    path('farmerRegister/<str:value>',views.registerf,name="register")
    
    
    
]
