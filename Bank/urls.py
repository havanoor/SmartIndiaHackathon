from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('ViewLoan/',views.LoanView,name='loanView'),
    path('makeloan/',views.makeloan,name='makeloan'),
    path('CreateLoan/',views.CreateLoan,name='CreateLoan')
    
    
    
    
]