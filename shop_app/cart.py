
class Cart: 
    def __init__(self, request): 
        self.request = request
        self.session = request.session 
        cart = self.session.get('cart', {})
        
        if not cart: 
            cart = self.session["cart"] = {}
        self.cart = cart
    
    # add a new product     
    def Add(self, product):
            
        if product.id not in self.cart:
            
            if product.Discount: 
                price = product.Discount
            else: 
                price = product.Price 
                
            self.cart[product.id] ={
                "Product_id": product.id, 
                "Name": product.Name, 
                "Price": float(price), 
                "precio": format(round(price*1000), ','),
                "Quantity": 1, 
                "Image": product.PrincipalImage.url,
                "Subtotal": format(price, '')
            }
        else: 
            for Key, Value in self.cart.items(): 
                if Key == product.id: 
                    Value["Quantity"] = Value["Quantity"] + 1 
                    break
                 
        self.Savecart()
    
     
    #  Save a cart to session                   
    def Savecart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
      
    # Delete a item of cart items   
    def DeleteItemcart(self, product):    
        id= str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.Savecart()
    
    # add a item cart
    def AddOne(self, product, quantity):

        id = str(product.id)
        
        for Key, Value in self.cart.items():
            
            if Key == id:
                if product.Discount: 
                    price= product.Discount
                else: 
                    price = product.Price 
                Value["Quantity"] = quantity + 1 
                Value["Subtotal"] = format(round(price * (quantity + 1 )*1000), ',')
                
        self.Savecart()

        
        
    #  substract a item of cart       
    def SubstractProduct(self, product, quantity):  
        
        id = str(product.id)
        
        for Key, Value in self.cart.items():
            
            if Key == id:
                if product.Discount: 
                    price= product.Discount 
                price = product.Price 
                
                if Value["Quantity"] < 1: 
                    self.DeleteItemcart(product) 
                               
                Value["Quantity"] = quantity - 1 
                Value["Subtotal"] = format(round(price * (quantity - 1 )*1000), ',')
                
                        
        self.Savecart()
        
    
    # Remove all cart items
    def Removecart(self):
        self.session["cart"] = {}
        self.session.modified = True
            
            
            
