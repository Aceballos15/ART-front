from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Image, Product
from django.urls import reverse 

from .cart import Cart
from . import forms 
# Create your views here.



class GetProductsView(View): 
    
    def get(self, request, user): 
        products = Product.objects.filter(Artisan= request.user)
        
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
        ProductEdit = get_object_or_404(Product, id=product)
        
        formEdit = forms.AddProductForm(instance=ProductEdit)
        return render(request, 'productos/AdminProductDetail.html', {'Products': products, 'form': formEdit})
    
    def post(self, request, product): 
        ProductEdit = Product.objects.get(id=product)
        form= forms.AddProductForm(data=request.POST, instance=ProductEdit, files=request.FILES)
        
        if form.is_valid(): 
            form.save(commit=False)
            form.Artisan = request.user.id
            
            form.save()
            
            return redirect(to = 'shop')
        
        
class CartView(View): 
    
    def get(self, request): 
        
        return render(request, 'Cart/CartShopping.html')
    
     
    
    
class WishListView(View): 
    
    def get(self, request): 
        return render(request, 'Cart/WishList.html') 
    
    
    
# Functions Cart 

def AddCartView(request, id):
    cart = Cart(request)
    prod= Product.objects.get(id=id)
    cart.Add(product=prod)
    
    return redirect(to= 'cart') 


def DeleteCartView(request): 
    cart = Cart(request)
    cart.Removecart()
    
    return redirect(to= 'cart')


def SubstractCartView(request, id, quantity): 
    cart = Cart(request)
    prod = Product.objects.get(id=id)
    cart.SubstractProduct(product=prod, quantity=quantity)
    
    return redirect(to= 'cart')


def DeleteItemCartView(request, id):
    cart = Cart(request)
    
    prod = Product.objects.get(id=id)
    
    cart.DeleteItemcart(product=prod)

    return redirect(to= 'cart')


def AddItemCartView(request, id, quant):
    
    cart = Cart(request)
    
    prod = Product.objects.get(id=id)
    
    cart.AddOne(product=prod, quantity=quant)
    
    return redirect(to= 'cart')


