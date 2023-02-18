from django.urls import path
from . import views 

urlpatterns = [
    path('productos/agregar', views.AddProductView.as_view(), name='AddProduct'),
    path('Shop/', views.ShopView.as_view(), name='shop'),
     path('Shop/<int:category>', views.CategoryView.as_view(), name='FilterCategory'),
    path('shop/details/<int:product>', views.ProductDetailView.as_view(), name='ProductDetail'),
    path('products/<int:user>', views.GetProductsView.as_view(), name= "ProductsUsers"),
    path('products/admin/<int:product>', views.AdminProductView.as_view(), name= "AdminProductDetail"), 
    
    
    # Cart
    path('cart/', views.CartView.as_view(), name= "cart"), 
    path('AddCart/<int:id>', views.AddCartView, name= "AddCart"),
    path('Delete/Cart/>', views.DeleteCartView, name= "DeleteCart"),
    path('cart/substract/<int:id>/<int:quantity>', views.SubstractCartView, name= "SubstractCart"),
    path('cart/DeleteItem/<int:id>', views.DeleteItemCartView, name= "DeleteItem"),
   path('cart/AddItem/<int:id>/<int:quant>', views.AddItemCartView, name= "addOne"),
   
   #WishList
   
    path('wishlist/', views.WishListView.as_view(), name= "wishlist"),
    
]
