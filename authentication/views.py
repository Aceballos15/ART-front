from django.shortcuts import render, redirect
from django.views import View
# Create your views here.
from . import forms
from django.contrib import messages
from .models import Users, Artisan

class RegisterView(View): 
    def get(self, request): 
        form= forms.CustomerRegistrationForm()
        return render(request, 'authenticate/Signup.html', {'form':form})

    def post(self, request):
        form= forms.CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request, 'authenticate/signup.html', {'form':form, 'error': 'La informacion no es valida, intenta Nuevamente'})
            

class profileView(View):
    def get(self, request):
        
        users= Users.objects.filter(User=request.user)
        
        if users:
            return render(request, 'profile_users/profile_detail.html', {'users': users})
        elif len(users) == 0:
            artisans= Artisan.objects.filter(User=request.user)
            if artisans:
                users= Artisan.objects.filter(User= request.user)
                return render(request, 'profile_users/profile_detail.html', {'users': artisans})
            
        form= forms.CustomersUsers()
        return render(request, 'profile_users/profile_user.html', {'form':form}) 
    
    
    def post(self, request):
        
        if request.POST['action'] == "comprar":
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
                
                return redirect('profile')

            else: 
                return render(request, 'profile/profile.html', {'form': form})
            
        else: 
            form = forms.CustomerArtisans(request.POST)
            if form.is_valid(): 
                Documento= form.cleaned_data['Documento']
                Name= form.cleaned_data['Name']
                Email= form.cleaned_data['Email']
                Adress= form.cleaned_data['Adress']
                Phone= form.cleaned_data['Phone']
                User =  request.user
                fm= Artisan(Documento=Documento, Name=Name, Email=Email, Adress=Adress, Phone=Phone, User=User)
                fm.save() 
                
                return redirect('profile')

            else: 
                return render(request, 'profile/profile.html', {'form': form})
            
        
         
class profileDetailView(View): 
    
    def get(self, request):
        pass
    
    def post(self, request): 
        pass