from django.db import models
from farmers.models import BankExecutive,Farmer
# Create your models here.

    

class Loan(models.Model):
    Publisher=models.ForeignKey(BankExecutive,on_delete=models.CASCADE)
    Amt=models.IntegerField()
    Rate=models.FloatField()
    Year=models.IntegerField()

class LoanIssue(models.Model):
    Issuer=models.ForeignKey(BankExecutive,on_delete=models.CASCADE)
    Issued_To= models.ForeignKey(Farmer,on_delete=models.CASCADE)
    Loan_Ref=models.ForeignKey(Loan,on_delete=models.CASCADE)
    Approved_Bank=models.BooleanField()
    Approved_Farmer=models.BooleanField()

