from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class UserProfileInfo(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)  
    username = models.CharField(max_length=25,null=True)  
    dob = models.DateField(blank=True,null=True) # If no date is selected then Django saves blank field value.  
    city = models.CharField(max_length=25,blank=True,null=True)
