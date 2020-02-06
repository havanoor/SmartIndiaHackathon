from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class NewUser(UserCreationForm):   
    email=forms.EmailField(label="",widget=forms.TextInput(

        attrs={'class':'us','placeholder':'Email'}
    ))
    post=forms.CharField(label="",widget=forms.TextInput(

        attrs={'class':'us','placeholder':'Post'}
    ))
    password2=forms.CharField(label="",widget=forms.PasswordInput(

        attrs={'class':'us','placeholder':' Confirm Password'}
    ))

    password1=forms.CharField(label="",widget=forms.PasswordInput(

        attrs={'class':'us','placeholder':'Password'}
    ))
    
    username=forms.CharField(label="",widget=forms.TextInput(

        attrs={'class':'us','placeholder':'Username'}
    )
    
    
    )


    class Meta: 
        model=User
        fields=['username','email','password1','password2','post']

class TransactionsForm(forms.ModelForm):
	class Meta:
		model=Transaction
		fields=('name','farm','seller')



#class BankForm(forms.ModelForm):
##		model=Bank
#		fields=('Weight','Water','Calorie')



class FarmerRegister(forms.ModelForm):
    class Meta:
        model=Farmer
        fields=['address','fstate','fdis']
