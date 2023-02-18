from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from shop_app.models import Product

def home(request):
    
    lista = Product.objects.all()[:6]
    return render(request, "home/index.html", {'lista': lista})


class ContactView(View):
    
    def get(self, request): 
        return render(request, "home/contact.html" ) 
        
    def post(self, request):
        User= request.POST['name']
        Email= request.POST['email']
        Message= request.POST['message'] + 'Enviado por: ' + User + ' ' + Email 
        
        email_from= Email
        send_mail(
            'Correo de Contacto', 
            Message, 
            email_from, 
            recipient_list= ['ceballoscardonaalexander@gmail.com'], 
            fail_silently= False
        )
        
        return redirect(to="home")

def login(request):
    return render(request, "authenticate/login.html")


def register(request):
    return render(request, "authenticate/Signup.html")


def AboutView(request):
    return render(request, "Home/Blog.html") 


