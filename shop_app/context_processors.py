

def Total_Cart(request):
    total = 0 
    
    if "cart" in request.session: 
        cart = request.session["cart"]
        for Key, Value in cart.items():
            
            total = total + ((float(Value["Price"])*1000) * Value["Quantity"])
            total = format(round(total), ',')
            
    return { "Total_Cart": total }





