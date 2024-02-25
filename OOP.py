print("TOTAL BILL CALCULATION")
class Item:
    pay_rate = 0.7
    def __init__(self,name:str,price:float,quantity: int = 0) :# Magic method+ data type
        print(f"An instance: {name}")

        #run validate input argument:
        assert price >= 0, f"Price {price} is not greater than 0"
        assert quantity >= 0,f"Quantity {quantity} is not greater than 0"
        #assign 
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def total_price(self):
        return self.price * self.quantity
#constructor:
    
item1 = Item("Phone",100,1)
print(item1.total_price())

item2 = Item("TV",1000,3)
print(item2.total_price())
print(Item.__dict__)#all attribute for Class level 
print(item1.pay_rate)
print(item2.pay_rate)
