from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.

#this view is to display all the current loans
def LoanView(request):
    q=Loan.objects.all()
    
    return render(request,'homeloan.html',{'loan':q})

#This view is used to create a loan for the farmer
def CreateLoan(request):
  try:
      u=BankExecutive.objects.get(Ref=request.user)
  except:
        return HttpResponse("Not ")
  return render(request,'loanform.html')
        

        

def makeloan(request):
    l=Loan()
    l.Amt=request.POST['amt']   
    l.Rate=request.POST['rate']
    l.Year=request.POST['year']
    l.Publisher=BankExecutive.objects.get(Ref=request.user)
    l.save()
    return HttpResponse('Done')     

    

