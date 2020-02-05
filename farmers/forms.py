from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class NewUser(UserCreationForm):   
    email=forms.EmailField()
    post=forms.CharField()



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




