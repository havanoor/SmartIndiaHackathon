from django.shortcuts import render,redirect
from .forms import NewUser
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    new=NewUser(request.POST)
    if new.is_valid():
        new.save()
        return redirect('login')
    else:
        new=NewUser()
    
    return render(request,'NewUser.html',{'form':new})


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
    return render(request, 'login.html', {'error': error})

@login_required
def home(request):
    return HttpResponse("Working")

