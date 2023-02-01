from django.db import models
from authentication.models import Artisan
# Create your models here.



class Product(models.Model):
    Name= models.CharField(max_length=255)
    Category= models.CharField(max_length=45)
    Description= models.TextField()
    Characteristics= models.TextField()
    stock= models.IntegerField(null=False)
    Price= models.DecimalField(max_digits=6, decimal_places= 3)
    Discount= models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    Images= models.ImageField(upload_to= 'products')
    Size= models.CharField(max_length=4, blank=True, null=True) 
    Gender= models.CharField(max_length=2, blank=True, null=True)
    Material= models.CharField(max_length= 50, blank=True, null=True)
    State= models.BooleanField(default=False)
    Artisan = models.ForeignKey(Artisan, on_delete=models.CASCADE, null=False)
    
    def __str__(self): 
        return self.Name
    
class Coment(models.Model):
    Qualification= models.IntegerField()
    Coment= models.CharField(max_length=255)
    Product= models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self): 
        return self.ID; 