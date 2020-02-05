from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns=[
    path('home',views.home,name='home'),
    path('CreateContract',views.create,name='CreateContract'),
    path('accept',views.accept,name='accept'),
    
]
