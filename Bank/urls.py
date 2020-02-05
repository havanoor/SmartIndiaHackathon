from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    #URL to view all the loans
    path('ViewLoan/',views.LoanView,name='loanView'),

    #URL to make new loan request
    path('CreateLoan/makeloan/',views.makeloan,name='makeloan'),

    #URL form for new loan
    path('CreateLoan/',views.CreateLoan,name='CreateLoan')
    
    
    
    
]