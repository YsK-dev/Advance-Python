class Product:
    def __init__(self,name,price):
        self.name=name
        if price >=0:
            self.price=price
        else:
            raise ValueError("PRİCE CANNOT BE NEGATIVE")
        
        @property
        def price(self):
            return self._price
        
        @price.setter
        def price(self, value):
            if value >=0:
                self._price = value
            else:
                raise ValueError("price cannot be negative")
    
'''    def setPrice(self,value):
        if value >=0:
            self._price = value
        else:
            raise ValueError("price cannot be negative")
        
    def getPrice(self):
        return self._price
   '''     
    

p = Product("Iphone 17",40004)
p.price = 4200
print(p.name,p.price)
