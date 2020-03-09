from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from datetime import datetime
from . forms import CreateDealer
from . models import *
from farmers.models import Dealer

# Create your views here.

def home(request):
    today=datetime.today()
    li=[]
    c=Contract.objects.all()
    for x in c:
        if x.Delivery >= today.date():
            print(x)
            li.append(x)
    
    
    return render(request,'home.html',{'y':li})

def create(request):
    try:
        u=User.objects.get(username=request.user)
        d=Dealer.objects.get(Ref=u)
        return render(request,'CreateContract.html')
    except:
        return HttpResponse("You havent been verified as a dealer  yet")



    
    






def accept(request):
    if request.method=='POST':
        i=request.POST['item']
        r=request.POST['Requirement']
        p=request.POST['Price']
        d=request.POST['Delivery']
        c=Contract(Publisher=request.user,Item=i,Requirement_Desc=r,Lock=p,Delivery=d)
        c.save()

        return HttpResponse("Success")
    else:
        return HttpResponse("F")
    