from django import forms

class CreateDealer(forms.Form):
    Address=forms.CharField(max_length=1000)
    Contact=forms.CharField(max_length=13)