from django.db import models

# Create your models here.



class Product(models.Model):
    Name= models.CharField(max_length=255)
    Category= models.CharField(max_length=45)
    Description= models.TextField()
    Characteristics= models.TextField()
    stock= models.models.IntegerField(min_value=0)
    Price= models.DecimalField(max_digits=6, decimal_places= 3)
    Discount= models.DecimalField(max_digits=6, decimal_places=3, blank=True)
    Images= models.ImageField(upload_to= 'products')
    Size= models.models.CharField(max_length=4, blank=True) 
    Gender= models.CharField(max_length=2, blank=True)
    Material= models.CharField(max_length= 50, blank=True)
    State= models.BooleanField(default=False)
    
    
class Coment(models.Model):
    Qualification= models.models.IntegerField()
    Coment= models.CharField(max_length=255)
    Product= models.ForeignKey(Product)