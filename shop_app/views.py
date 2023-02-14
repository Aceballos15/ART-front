from django.shortcuts import render
from django.views import View
from .models import Image, Product

from . import models 
from . import forms 
# Create your views here.


class GetProductsView(View): 
    
    def get(self, request, user): 
        products = Product.objects.filter(Artisan= user)
        
        return render(request, 'productos/ViewProducts.html', {'products': products})

class AddProductView(View): 
    
    def get(self, request, *args, **kwargs):
        
        form = forms.AddProductForm()
        return render(request, 'productos/AddProduct.html', { 'form': form }) 
        
        
    def post(self, request, *args, **kwargs):  
        
        form = forms.AddProductForm(request.POST, request.FILES)
        files= request.FILES.getlist('Images')
        
        if form.is_valid():
            New_Product= form.save(commit=False)
            New_Product.Artisan = request.user 
            New_Product.save()
            
            for i in files:
                img = Image(Image = i)
                img.save()
                
                New_Product.Images.add(img)
                
            New_Product.save()
            
        else: 
            return render(request, 'productos/AddProduct.html', { 'form': form })
    
class EditProductView(View):
    
    def get(self, request): 
        pass 
    
    
    
class ShopView(View):
    
    def get(self, request): 
        
        Products= Product.objects.all()
        
        return render(request, 'home/shop.html', {'Products': Products})

    
    
    def post(self, request, *args, **kwargs):
        pass
    
    
class ProductDetailView(View):
    
    def get(self, request, product): 
        
        products= Product.objects.filter(id=product)
        
        return render(request, 'productos/ProductDetail.html', {'Products': products})
    
    def post(self, request, *args, **kwargs):
        pass
    
    
    
    
class AdminProductView(View): 
    
    def get(self, request, product): 
        products= Product.objects.filter(id=product)
        return render(request, 'productos/AdminProductDetail.html', {'Products': products})
    
    def post(self, request, *args, **kwargs): 
        pass