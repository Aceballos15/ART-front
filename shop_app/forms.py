from .models import Product
from django import forms 



Gender= [
    ('N', 'No aplica'),
    ('F', 'Femenino'), 
    ('M', 'Masculino'),
    ('U', 'Unisex')
]
Sizes= [
    ('NA', 'No aplica'),
    ('XS', 'XS'),
    ('S', 'S'),
    ('M', 'M'),
    ('L', 'L'),
    ('XL', 'XL'),
    ('XXL', 'XXL')
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

class AddProductForm(forms.ModelForm):
     
    Name= forms.CharField(label= 'Nombre', widget= forms.TextInput(attrs={ 'class': 'theme-input-style', 'required': 'True', 'placeholder': 'Nombre del producto'}))
    Stock = forms.IntegerField(label= 'Disponibilidad', widget= forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required': True , 'placeholder': 'Cantidad disponible', 'min': 1, 'value': 1 }))
    Price = forms.DecimalField(label= 'Precio', widget= forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required':True, 'placeholder': 'Precio'}))
    Discount= forms.DecimalField(label= 'Precio con descuento', widget= forms.NumberInput(attrs={ 'class': 'theme-input-style', 'required':True, 'placeholder': 'Precio del descuento (Opcional)'}))
    Category= forms.ChoiceField(choices= Categories, label= 'Categoria', widget= forms.Select(attrs={ 'class': 'theme-input-style', 'required':True, 'placeholder': 'Categorias'}))
    Material= forms.CharField(label= 'Material', widget= forms.TextInput(attrs={ 'class': 'theme-input-style', 'required':True, 'placeholder': 'Material de fabrica'}))
    Gender = forms.ChoiceField(choices=Gender, label= 'Genero', widget= forms.Select(attrs={ 'class': 'theme-input-style', 'required': False, 'placeholder': 'Genero (Opcional)'}))
    Size = forms.ChoiceField(choices= Sizes, label= 'Tallas', widget= forms.Select(attrs={ 'class': 'theme-input-style', 'required': False, 'placeholder': 'Tallas (Opcional)'}))
    Description= forms.CharField(label= 'Descripcion', widget=  forms.Textarea(attrs={ 'class': 'theme-input-style', 'required': True}))
    Characteristics= forms.CharField(label= 'Caracteristicas del producto', widget= forms.Textarea(attrs={ 'class': 'theme-input-style', 'required': False}))
    Images = forms.FileField(label= 'Imagenes del producto', widget= forms.ClearableFileInput(attrs={ 'multiple':True , 'class': 'theme-input-style', 'required': 'True'})) 
    PrincipalImage= forms.FileField(label= 'Portada del producto', widget= forms.ClearableFileInput(attrs={ 'multiple':True , 'class': 'theme-input-style', 'required': 'True'})) 
    
    class Meta: 
        model = Product
        fields = ['Name', 'Category', 'Description', 'Characteristics', 'Stock', 'Price', 'Discount', 'Images', 'Size', 'Gender', 'Material', 'PrincipalImage']
        
