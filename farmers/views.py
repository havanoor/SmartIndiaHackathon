from django.shortcuts import render,redirect
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from twilio.rest import Client
# Create your views here.


def register(request):
    

    
    new=NewUser(request.POST)
    if new.is_valid():
        new.save()
        user = authenticate(username=new.cleaned_data['username'], password=new.cleaned_data['password1'])
        if user is not None:
            login(request, user)
        type1=new.cleaned_data['post']
        if type1.lower()=='farmer':
            
            return redirect('/farmerRegister/farmer')
           
        elif type1.lower()=='seller':
            return render(request,'register.html',{'type':type1.lower()})
        elif type1.lower()=='dealer':
            return render(request,'register.html',{'type':type1.lower()})
        elif type1.lower()=='bankexecutive':
            return render(request,'register.html',{'type':type1.lower()})
        

        return redirect('home')
        
    else:
        new=NewUser()
     
    return render(request,'NewUser.html',{'form':new})


def registerf(request,value):
    if value=='farmer':
        form=FarmerRegister(request.POST)
        if request.method=='POST':
            if form.is_valid():
                f=Farmer(fidentity=request.user,address=form.cleaned_data.get('address'),fstate=form.cleaned_data.get('fstate'),fdis=form.cleaned_data.get('fdis'))
                f.save()
                return redirect('home')
                #account_sid = "ACdba2322fbfb7f799611ab1393126afc9"
                #auth_token  =  "1196ac8c07c05bb98053f602bcb4236a"
                #client = Client(account_sid, auth_token)

                #message = client.messages.create(

                #to="+91{}".format(f.contact),
                #from_="+12074050731",
                #body="Registered as a Farmer -Team 404"
            #)
            else:
                return render(request,'farmerRegister.html',{'form':form})

        else:
            return render(request,'farmerRegister.html',{'form':form})

    else:
        if request.method=='POST':
        
            if value=='dealer':
        
                d=Dealer()
                d.Ref=request.user
                d.Address=request.POST['address']
                d.Contact=request.POST['contact']
                d.save()
                
            
            elif value=='seller':
        
                s=Seller()
                s.sidentity=request.user
                s.address=request.POST['address']
                s.Contact=request.POST['contact']
                
                s.save()
            elif value == 'bankexecutive':
                b=BankExecutive()
                b.Ref=request.user
                b.Address=request.POST['address']
                b.Contact=request.POST['contact']
                
                b.save()

    return HttpResponse('Created')





            

        
        





def loginUser(request):
    error=None
    if request.method == 'POST':
        username =request.POST['username']
        passw =request.POST['password']
        user = authenticate(username=username, password=passw)
        if user is not None:
            login(request, user) # logs User in
            return redirect('home')
        else:
            #return render(request, 'signup.html', {'error': "Unable to Log you in!"})
            error="Try again"
    return render(request, 'loginSIH.html', {'error': error})

@login_required
def home(request):

    return render(request,'home.html')

def withdraw(request,value):
    if value=='withdraw':
        return render(request,'withdraw.html',{'val':'withdraw'})



def calculate(request,value):
    
    farmer=Farmer.objects.filter(fidentity=request.user).first()
    print(farmer)
    if value=='withdraw':
        farmer.balance -= int(request.POST['val'] )
    farmer.save()
    return redirect('home')

def transaction(request,obj_id):
    request.session['k']=obj_id
    p=request.session['k']
    print(p)
    i=Inventory.objects.get(id=obj_id)

    
    cost=i.amount
    
    return render(request,"purchase.html",{'cost':cost})

def Success(request):
    key=request.session['k']
    
    print(key)
    print(key)

    return HttpResponse(key)




    

def purchase(request):
    a=Inventory.objects.all()
    
    return render(request,'marketplace.html',{'val':a})



    

