from .models import Product
from django import forms 

class AddProductForm(forms.ModelForm):
    class Meta: 
        
        model = Product
        fields = ['Name', 'Category', 'Description', 'Characteristics', 'Stock', 'Price', 'Discount', 'Images', 'Size', 'Gender', 'Material']
        
        widgets = {
            'Name': forms.TextInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Nombre del producto'}), 
            'Stock': forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Cantidad disponible', 'min': 1, 'value': 1 }),
            'Price': forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Precio'}),  
            'Discount': forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Precio del descuento (Opcional)'}), 
            'Category': forms.Select(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Categorias'}),  
            'Material': forms.TextInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Material de fabrica'}), 
            'Gender': forms.Select(attrs={ 'class': 'theme-input-style', 'required': 'False', 'placeholder': 'Genero (Opcional)'}), 
            'Size': forms.Select(attrs={ 'class': 'theme-input-style', 'required': 'False', 'placeholder': 'Tallas (Opcional)'}), 
            'Description': forms.Textarea(attrs={ 'class': 'theme-input-style', 'required': 'True'}), 
            'Characteristics': forms.Textarea(attrs={ 'class': 'theme-input-style', 'required': 'False'}), 
            'Images': forms.FileInput(attrs={ 'class': 'theme-input-style', 'required': 'True'}), 
        }