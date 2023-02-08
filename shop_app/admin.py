from django.contrib import admin

# Register your models here.
from .models import Product, Image 


admin.site.register(Product) 

admin.site.register(Image)