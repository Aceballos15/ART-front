from django.shortcuts import render 



def home(request):
    return render(request, "home/index.html")

def shop(request): 
    return render(request, "home/shop.html") 