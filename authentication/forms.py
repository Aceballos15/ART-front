from django import forms 

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm

from django.contrib.auth.models import User

from .models import Users

class CustomerRegistrationForm(UserCreationForm):
    
    username = forms.CharField(label='Usuario', widget=forms.TextInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Usuario', 'required': 'true'}))
    email= forms.CharField(label='Correo Electronico', widget=forms.EmailInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Correo electronico', 'required': 'true'}))
    password1= forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Contraseña', 'required': 'true'}))
    password2= forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Confirmar contraseña', 'required': 'true'}))
    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        
class LoginForm(AuthenticationForm): 
    
    username= forms.CharField(label='Usuario', widget=forms.TextInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Usuario', 'required': 'true'}))
    
    password= forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs= {'class': 'theme-input-style', 'placeholder': 'Contraseña', 'required': 'true'}))
    
    class Meta: 
        model= User 
        fields= ['username', 'password']
        
class PasswordResetForm(PasswordChangeForm):
    pass 



class CustomersUsers(forms.ModelForm): 
    class Meta:
        model = Users
        fields = ['Documento', 'Name', 'Email', 'Adress', 'Phone']
        
        widgets = {
            'Documento': forms.NumberInput(attrs={'class': 'theme-input-style', 'placeholder': 'Documento de identidad', 'required': 'true'}),
            'Name': forms.TextInput(attrs={'class': 'theme-input-style', 'placeholder': 'Nombre y apellidos', 'required': 'true'}),
            'Email': forms.TextInput(attrs={'class': 'theme-input-style', 'placeholder': 'Correo Electronico', 'required': 'true'}),
            'Adress': forms.TextInput(attrs={'class': 'theme-input-style', 'placeholder': 'Direccion', 'required': 'true'}),
            'Phone': forms.NumberInput(attrs={'class': 'theme-input-style', 'placeholder': 'Numero de telefono', 'required': 'true'}),
        }
        