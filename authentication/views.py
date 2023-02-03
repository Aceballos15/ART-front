from django.shortcuts import render
from django.views import View
# Create your views here.
from . import forms
from django.contrib import messages


class RegisterView(View): 
    
    def get(self, request): 
        form= forms.CustomerRegistrationForm()
        return render(request, 'authenticate/Signup.html', {'form':form})

    def post(self, request):
        form= forms.CustomerRegistrationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request, 'home/index.html')
        else:
            return render(request, 'authenticate/signup.html', {'form':form, 'error': 'La informacion no es valida, intenta Nuevamente'})
            

class profileView(View):
    def get(self, request):
        form= forms.CustomersUsers()
        return render(request, 'profile/profile.html', {'form':form}) 
    
    def post(self, request):
        
        form= forms.CustomersUsers(request.POST)
        
        if form.is_valid():
            form.save(commit=False)
            
            form.Role = '1'
            form.User = request.user
            
            form.save()
            return render(request, 'home/index.html') 
        
        else: 
            return render(request, 'profile/profile.html', { 'form': form, 'error': form.errors })