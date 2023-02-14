from django.urls import path
from . import views 

urlpatterns = [
    path('productos/agregar', views.AddProductView.as_view(), name='AddProduct'),
    path('Shop/', views.ShopView.as_view(), name='shop'),
    path('shop/details/<int:product>', views.ProductDetailView.as_view(), name='ProductDetail'),
    path('products/<int:user>', views.GetProductsView.as_view(), name= "ProductsUsers"),
    path('products/admin/<int:product>', views.AdminProductView.as_view(), name= "AdminProductDetail")

]
