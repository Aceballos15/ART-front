from django.shortcuts import render 



def home(request):
    lista= [0,1 ,2 ,3, 4, 5 ]
    return render(request, "home/index.html", {'lista': lista})

def shop(request): 
    lista= [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    return render(request, "home/shop.html", {"lista": lista}) 

def login(request):
    return render(request, "authenticate/login.html")


def register(request):
    return render(request, "authenticate/Signup.html")