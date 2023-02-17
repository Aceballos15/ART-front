

def Total_Cart(request):
    total = 0 
    
    if "cart" in request.session: 
        cart = request.session["cart"]
        for Key, Value in cart.items():
            price = Value["Price"] * 1000
            
            total = float(total) + ( price * Value["Quantity"] )  
            total = round(total)
            
            
    return { "Total_Cart": format(total, ',') }





