class CartItem:
    itemCount = 0

    @classmethod
    def displayCount(cou):
        return f"{CartItem.itemCount} stock created"
    @classmethod
    def createItem(cou,dataS):
        name ,price ,quantity =dataS.split(",")
        return cou(name,price,quantity)

    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        CartItem.itemCount +=1
    #İnstance Method 
    def calculateTotal(self):
        return self.price * self.quantity
    
    def applyDiscount(self,rate):
        self.price = self.price * rate

    def __str__(self):
        return f"CartItem(Name: {self.name}, Price: {self.price}, Quantity: {self.quantity})"


print(CartItem.displayCount())
item0= CartItem("honda",25000,1)
item1 = CartItem("RkS",2300,2)
item2 = CartItem("TwS",204,2)
CartItem.createItem("MErcedes,300902903,1 ")
print(item0.name)
print(CartItem("TOROS",3,45))
print(CartItem.displayCount())     

class Coupon:
    def __init__(self,code,discount):
        self.code = code
        self.discount = discount

    def __str__(self):
        return f"Coupon(Code: {self.code}, Discount: {self.discount})"

    


class shoppingCart:
    couponLists = [
        Coupon("code1",0.8),
        Coupon("code2",0.7),
        Coupon("code3",0.6),
    ]
    def __init__(self,lists):
        self.lists=lists

    def addItem(self,item):
        self.lists.append(item)

    def displayItem(self):
        return "\n".join([f"{item.name} - {item.price}" for item in self.lists])
        
    def calculateTotalS(self):
        return sum([item.calculateTotal() for item in self.lists])
    
    def removeItem(self,item):
        self.lists=[item for item in self.lists if item !=CartItem]

    def Clear(self):
        self.lists=[]

    @classmethod
    def getCoupons(cls):
        return [coupon.code for coupon in cls.couponLists]
    
    @classmethod
    def getCoupon(cls,code):
        return next((c for c in cls.couponLists if c.code == code), None)
    
    def applyCoupon(self,code):
        if code not in shoppingCart.getCoupons():
            raise ValueError(f"Invalid coupon code --> {code}")
        
        coupon =shoppingCart.getCoupon(code)
        for index in range(0,len(self.lists)):
            self.lists[index].price = self.lists[index].price * coupon.discount


# Test the ShoppingCart class
item0 = CartItem("honda", 25000, 1)
item1 = CartItem("RkS", 2300, 2)
item2 = CartItem("TwS", 204, 2)

sc = shoppingCart([item0, item1])
sc.addItem(item2)

# Display items
print("Items in cart:")
print(sc.displayItem())

# Calculate total before coupon
print(f"\nTotal before coupon: {sc.calculateTotalS()}")

# Apply coupon
sc.applyCoupon("code1")
print("\nItems after applying coupon:")
print(sc.displayItem())

# Calculate total after coupon
print(f"\nTotal after coupon: {sc.calculateTotalS()}")

# Remove an item
sc.removeItem(item1)
print("\nItems after removing RkS:")
print(sc.displayItem())

