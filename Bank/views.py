from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
# Create your views here.


def LoanView(request):
    q=Loan.objects.all()
    
    return render(request,'homeloan.html',{'loan':q})

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
    l.Publisher=request.user
    l.save()
    return HttpResponse('Done')     

    

