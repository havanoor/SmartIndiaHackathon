from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponse
from django.core.mail import send_mail
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
        

def processLoan(request):
    
    try:
        u=BankExecutive.objects.get(Ref=request.user)
    except:
        return HttpResponse('Not Authorised')

    form=ProcessLoan(request.POST)  
    if request.method=='POST':
        
        
        if form.is_valid():
            k=form.cleaned_data.get('Loan_Ref')
            print(k.Publisher)
            

            l=LoanIssue(Issuer=u,Issued_To=form.cleaned_data.get('Issued_To'),Loan_Ref=form.cleaned_data.get('Loan_Ref'),Approved_Bank=True,Approved_Farmer=False)
            l.save()
            print(l.id)
            send_mail('Loan','Please Verify that you have issued loan http://127.0.0.1:8000/Bank/verify/{}'.format(l.id),'hrishikesh2pv@gmail.com',['shahjash271@gmail.com'],fail_silently=False)
            return HttpResponse('Bank Done')
        else:
            return render(request,'processLoan.html',{'form':form})
    return render(request,'processLoan.html',{'form':form})
    


        

def makeloan(request):
    l=Loan()
    l.Amt=request.POST['amt']   
    l.Rate=request.POST['rate']
    l.Year=request.POST['year']
    l.Publisher=BankExecutive.objects.get(Ref=request.user)
    l.save()
    return HttpResponse('Done')     

    

def verify(request,obj_id):
    try:
        print("Hello")
        print(request.user)
        f=Farmer.objects.get(fidentity=request.user)
        #k=Farmer.objects.filter(fidentity=request.user).first()
        print(f)
        
    except:
        return HttpResponse("No")
    l=LoanIssue.objects.get(id=obj_id)
    l.Approved_Farmer=True
    l.save()
    return HttpResponse ('Done')