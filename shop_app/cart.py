
class Cart: 
    def __init__(self, request): 
        self.request = request
        self.session = request.session 
        cart = self.session.get('cart', {})
        
        if not cart: 
            cart = self.session["cart"] = {}
        self.cart = cart
         
    def Add(self, product):
            
        if product.id not in self.cart:
            self.cart[product.id] ={
                "Product_id": product.id, 
                "Name": product.Name, 
                "Price": str(product.Price), 
                "Quantity": 1, 
                "Image": product.PrincipalImage.url
            }
        else: 
            for Key, Value in self.cart.items(): 
                if Key == product.id: 
                    Value["Quantity"] = Value["Quantity"] + 1 
                    break
                 
        self.Savecart()
    
                        
    def Savecart(self):
        self.session["cart"] = self.cart
        self.session.modified = True
    
        
    def DeleteItemcart(self, product):    
        id= str(product.id)
        if id in self.cart:
            del self.cart[id]
            self.Savecart()
    
            
    def SubstractProduct(self, product):  
        for Key, Value in self.cart.items():
            
            if Key == product.id:
                Value["Quantity"] = Value["Quantity"] - 1 
                if Value["Quantity"] < 1: 
                    self.DeleteItemcart(product)
                break 
        self.Savecart()
        
    
    def Removecart(self):
        self.session["cart"] = {}
        self.session.modified = True
            
            
            
