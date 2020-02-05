from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#details of the farmer
class Farmer(models.Model):
    fidentity=models.OneToOneField(User,on_delete=models.CASCADE)
    Dob=models.DateField()
    address=models.CharField(blank=False,max_length=200)
    #owner=models.OneToOneField(User,on_delete=models.CASCADE)
    balance=models.IntegerField(default=0)


#details of the seller
class Seller(models.Model):
    sidentity=models.OneToOneField(User,on_delete=models.CASCADE)
    address=models.CharField(blank=False,max_length=200)
    itemssold=models.CharField(blank=False,max_length=200)


    


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
    photo=models.ImageField()


#this class handles all the transactions between farmer and the seller
class Transaction(models.Model):
    name=models.ForeignKey(Inventory,on_delete=models.CASCADE)
    farm=models.ForeignKey(Farmer,on_delete=models.CASCADE)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)



     
    
    


 

    