from django.shortcuts import render
from django.views import View
# Create your views here.
from . import forms
from django.contrib import messages
from .models import Users 

class RegisterView(View): 
    
    def get(self, request): 
        form= forms.CustomerRegistrationForm()
        return render(request, 'authenticate/Signup.html', {'form':form})

    def post(self, request):
        form= forms.CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'authenticate/login.html')
        else:
            return render(request, 'authenticate/signup.html', {'form':form, 'error': 'La informacion no es valida, intenta Nuevamente'})
            

class profileView(View):
    def get(self, request):
        form= forms.CustomersUsers()
        return render(request, 'profile/profile.html', {'form':form}) 
    
    def post(self, request):
        
        form = forms.CustomersUsers(request.POST)
        
        if form.is_valid(): 
            
            Documento= form.cleaned_data['Documento']
            Name= form.cleaned_data['Name']
            Email= form.cleaned_data['Email']
            Adress= form.cleaned_data['Adress']
            Phone= form.cleaned_data['Phone']
            Role= 1 
            User =  request.user
            fm= Users(Documento=Documento, Name=Name, Email=Email, Adress=Adress, Phone=Phone, Role=Role, User=User)
            fm.save()
            
            return render(request, 'home/index.html')
        else: 
            return render(request, 'profile/profile.html', {'form': form}) 
        
        