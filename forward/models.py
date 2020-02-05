from django.db import models
from farmers.models import Dealer

# Create your models here.
class Contract(models.Model):
    Publisher=models.ForeignKey(Dealer,on_delete=models.CASCADE)
    
    Item=models.TextField()
    Requirement_Desc=models.TextField()
    Lock=models.IntegerField()
    Delivery=models.DateField()