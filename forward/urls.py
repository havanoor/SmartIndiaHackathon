from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns=[
    #Homepage of forward market
    path('home',views.home,name='homeForward'),

    #Create a new contract between dealer and farmer
    path('CreateContract',views.create,name='CreateContract'),

    #
    path('accept',views.accept,name='accept'),
    
]
