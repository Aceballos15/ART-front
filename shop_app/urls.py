from django.urls import path
from . import views 

urlpatterns = [
    path('productos/agregar', views.AddProductView.as_view(), name='AddProduct'),
]
