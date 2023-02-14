from django.shortcuts import render, redirect
from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    lista= [0,1 ,2 ,3, 4, 5 ]
    return render(request, "home/index.html", {'lista': lista})


class ContactView(View):
    
    def get(self, request): 
        return render(request, "home/contact.html" ) 
        
    def post(self, request):
        User= request.POST['name']
        Email= request.POST['email']
        Message= request.POST['message']
        
        email_from= Email
        send_mail(
            'Correo de Contacto', 
            Message, 
            email_from, 
            recipient_list= ['ceballoscardonaalexander@gmail.com'], 
            fail_silently= False
        )
    
        messages.success(request, "Envio de formulario correctamente")
        return redirect(to="contact")

def login(request):
    return render(request, "authenticate/login.html")


def register(request):
    return render(request, "authenticate/Signup.html")