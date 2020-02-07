from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class State(models.Model):
    sname=models.CharField(max_length=100,blank=None)
    def __str__(self):
        return self.sname


class District(models.Model):
    dname=models.CharField(max_length=100,blank=None)
    sref=models.ForeignKey(State,on_delete=models.CASCADE)
    ph=models.FloatField(blank=False)
    N=models.FloatField(blank=False)
    P=models.FloatField(blank=False)
    K=models.FloatField(blank=False)
    OC=models.FloatField(blank=False)
    Fe=models.FloatField(blank=False)
    

    def __str__(self):
        return self.dname




class CropStats(models.Model):
    dref=models.ForeignKey(District,on_delete=models.CASCADE)
    ph=models.ImageField(upload_to='photos/')
    N=models.ImageField(upload_to='photos/')
    P=models.ImageField(upload_to='photos/')
    K=models.ImageField(upload_to='photos/')
    OC=models.ImageField(upload_to='photos/')
    Fe=models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.dref.dname




#details of the farmer
class Farmer(models.Model):
    fidentity=models.OneToOneField(User,on_delete=models.CASCADE)
   
    address=models.CharField(blank=False,max_length=200)
    
    balance=models.IntegerField(default=0)
    fstate=models.ForeignKey(State,on_delete=models.CASCADE)
    fdis=models.ForeignKey(District,on_delete=models.CASCADE)
    contact=models.CharField(max_length=10)

    def __str__(self):
        return self.fidentity





#details of the seller
class Seller(models.Model):
    sidentity=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(blank=False,max_length=200)
    itemssold=models.CharField(blank=False,max_length=200)
    Contact=models.CharField(max_length=13,blank=False)
    def __seller__(self):
        return self.sidentity


    


#This models handles the Loan's take by the farmer 
class Loan(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    pendingA=models.IntegerField(default=0)



#This is the inventory class that contains all the goods in the marketplace
class Inventory(models.Model):
    name=models.CharField(blank=False,max_length=100)
    Type=models.CharField(blank=False,max_length=100)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    amount=models.IntegerField(blank=False)
    photo=models.ImageField(upload_to='media')

    def __str__(self):
        return self.name



#this class handles all the transactions between farmer and the seller
class Transaction(models.Model):
    name=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    farm=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Dealer(models.Model):
    Ref=models.ForeignKey(User,on_delete=models.CASCADE)
    
    Address=models.TextField()
    Contact=models.CharField(max_length=10)

    def __str__(self):
        return self.Ref.username

	

class BankExecutive(models.Model):
    Ref=models.ForeignKey(User,on_delete=models.CASCADE)
    Bank_Name=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    Contact=models.IntegerField()

    def __str__(self):
        return self.Ref.username











     
    
    


 

    