from django.db import models
from authentication.models import Artisan
# Create your models here.


Sizes= [
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL')
]

Gender= [
    ('F', 'Femenino'), 
    ('M', 'Masculino'),
    ('U', 'Unisex')
]

Categories = [
    (1, 'Artesania Indigena'), 
    (2, 'Pinturas'), 
    (3, 'Bordados'), 
    (4, 'Tejidos'), 
    (5, 'Carpinteria'), 
    (6, 'Alfareria'), 
    (7, 'artesania Reciclada'), 
    (8, 'Decoracion y regalos'), 
    (9, 'Otra')
      
]

class Product(models.Model):
    Name= models.CharField(max_length=255)
    Category= models.IntegerField(choices= Categories)
    Description= models.TextField(max_length= 256 )
    Characteristics= models.TextField(max_length= 500 )
    Stock= models.IntegerField(null=False)
    Price= models.DecimalField(max_digits=6, decimal_places= 3)
    Discount= models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    Images= models.ImageField(upload_to= 'products')
    Size= models.CharField(max_length=4, blank=True, null=True, choices= Sizes) 
    Gender= models.CharField(max_length=2, blank=True, null=True, choices=Gender)
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