from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Users(models.Model):
    Documento= models.IntegerField(null=False)
    Name= models.CharField(max_length=255, null=False, blank=False)
    Email= models.EmailField(max_length=255, null=False, blank=False)
    Adress= models.CharField(max_length=255, blank=False, null=False)
    Role= models.CharField(max_length=2, blank=False, null=False)
    Phone= models.IntegerField()
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
       return self.name
   
   
class Artisan(models.Model):
    Documento= models.IntegerField(null=False)
    Name= models.CharField(max_length=255, null=False, blank=False)
    Email= models.EmailField(max_length=255, null=False, blank=False)
    Adress= models.CharField(max_length=255, blank=False, null=False)
    Image= models.ImageField(upload_to='artisans')
    Phone= models.IntegerField()
    Number_bank= models.IntegerField(null=True)
    Bank= models.CharField(max_length=45, null=True, blank=True)
    State= models.BooleanField(default=False)
    User= models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.name