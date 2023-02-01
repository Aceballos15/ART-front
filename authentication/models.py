from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):
    Documento= models.IntegerField(null=False)
    Name= models.CharField(max_length=255, null=False, blank=False)
    Email= models.EmailField(max_length=255, null=False, blank=False)
    adress= models.CharField(max_length=255, blank=False, null=False)
    Role= models.CharField(max_length=2, blank=False, null=False)
    Phone= models.IntegerField()
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.name
   
   
class Artisan(models.Model):
    Documento= models.IntegerField(null=False)
    Name= models.CharField(max_length=255, null=False, blank=False)
    Email= models.EmailField(max_length=255, null=False, blank=False)
    adress= models.CharField(max_length=255, blank=False, null=False)
    Image= models.ImageField(upload_to='artisans')
    Phone= models.IntegerField()
    Number_bank= models.IntegerField(null=False)
    Bank= models.CharField(max_length=45, null=False, blank=False)
    state= models.BooleanField(default=False)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.name