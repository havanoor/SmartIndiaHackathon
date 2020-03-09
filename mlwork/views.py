from django.shortcuts import render,redirect
from farmers.models import *
from django.contrib.auth.models import User
from django.http import HttpResponse
from .views2 import *

# Create your views here.


def MachineHome(request):
    Xaxis=[]
    Yaxis=[]
    farm=Farmer.objects.get(fidentity=request.user)
    dis=farm.fdis
    stats=District.objects.get(dname=dis)
    phval=stats.ph
    Nval=stats.N
    Pval=stats.P
    Kval=stats.K
    OCval=stats.OC
    Feval=stats.Fe
    rainval=stats.rainfall
    l1=[phval,Nval,Pval,Kval,OCval,Feval]
    temp=weath(dis)
    l1.append(temp[0])
    l1.append(temp[1])
    final_result=yield_calculate(l1)

    for i in final_result[0]:
        Xaxis.append(i)
    for j in final_result[1]:
        Yaxis.append(j[0])

    print(Yaxis)

    return render(request,"MachineHome.html",{"Xaxis":Xaxis,"Yaxis":Yaxis})
    

