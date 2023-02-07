from django.shortcuts import render
from django.views import View

from . import forms 
# Create your views here.

class AddProductView(View): 
    
    def get(self, request):
        
        form = forms.AddProductForm()
        return render(request, 'productos/AddProduct.html', { 'form': form }) 
        
        
    
    def post(self, request): 
        pass
    
    
class EditProductView(View):
    
    def get(self, request): 
        pass 
    
    
    