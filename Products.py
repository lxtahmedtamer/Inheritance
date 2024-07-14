from abc import ABC, abstractmethod
class AbstractProduct(ABC):
    
    @abstractmethod
    def set_product_name(self, name):
        pass

    @abstractmethod
    def get_product_name(self):
        pass    

    @abstractmethod
    def set_amount(self, amount):
        pass

    @abstractmethod
    def get_amount(self):
        pass

   


    @abstractmethod
    def product_price(self):
        pass

    @abstractmethod
    def product_payment(self):
        pass

class Product(AbstractProduct):
    

    def set_product_name(self, name):
        self.product_selection:str
        self.product_selection = name

    def get_product_name(self):
        return self.product_selection

    def set_amount(self, amount):
        self.amount = float(amount)  # Convert input to float

    def get_amount(self):
        return self.amount

    def product_price(self):
        if self.product_selection == "Hot Drink":
            self.cost = 20
        elif self.product_selection == "Cold Drink":
            self.cost = 30
        elif self.product_selection == "Snack":
            self.cost = 40
        elif self.product_selection == "Ice Cream":
            self.cost = 50    
        print(f"Price for {self.product_selection}: ${self.cost}")    

    def product_payment(self,b):
        no3=b
        budget = self.get_amount()  # Get amount as float
        while budget <= 0:
            budget = float(input("Invalid amount. Please insert a positive amount: "))
        
        while budget < self.cost:
            budget = float(input(f"Please insert enough money to buy {self.product_selection}: "))
        
        self.money_rest = budget - self.cost
        print(f"you have chosen {no3}")   
        print("Your remaining money =", self.money_rest)   
        print("Thank you for using the Vending Machine!")   
class HotDrink(Product):
    def HotDrink_Menu(self,product_name):
        HotDrink_list = ["Tea", "Nescafe", "Hot Chocolate"]
        y=input(print("Choose one of Hot Drinks available:", HotDrink_list))
        while y not in  ColdDrink_list :
           print("WRONG, Choose one of Hot Drinks available:",HotDrink_list)
           y =input()
        
        self.product_selection=product_name
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment(y)
class ColdDrink(Product):
    
   
    def ColdDrink_Menu(self,product_name):
        ColdDrink_list = ["Pepsi", "Seven up", "Mirinda"]
       
        y=input(print("Choose one of Cold Drinks available:", ColdDrink_list))
        while y not in  ColdDrink_list :
           print("WRONG, Choose one of Cold Drinks available:",ColdDrink_list)
           y =input()
        
        self.product_selection=product_name
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment(y)

class Snack(Product):
    
    
    def Snack_Menu(self,product_name):
        Snack_list = ["Chipsy", "Cheetos", "Doritos"]
        y=input(print("Choose one of Snacks available:", Snack_list))
        while y not in  Snack_list :
           print("WRONG, Choose one of Snacks available:",Snack_list)
           y =input()
        
        self.product_selection=product_name
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment(y)

class Icecream(Product):
    
    def Icecream_Menu(self,product_name):
        Icecream_list = ["Chocolate", "Vanilla", "Strawberry"]
        y=input(print("Choose one of Flavors available:", Icecream_list))
        while y not in  Icecream_list :
           print("WRONG, Choose one of Snacks available:",Icecream_list)
           y =input()
        
        self.product_selection=product_name
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment(y)

# Main Product selection
obj = Product()
obj.set_product_name("Snack")

if obj.get_product_name() == "Hot Drink":
    hot_obj = HotDrink()
    x=obj.get_product_name()
    hot_obj.HotDrink_Menu(x)
    
    
elif obj.get_product_name() == "Cold Drink":
    cold_obj = ColdDrink()
    x=obj.get_product_name()
    cold_obj.ColdDrink_Menu(x)
   
    
elif obj.get_product_name() == "Snack":
    snack_obj = Snack()
    x=obj.get_product_name()
    snack_obj.Snack_Menu(x)

    
elif obj.get_product_name() == "Ice Cream":
    icecream_obj = Icecream()
    x=obj.get_product_name()
    icecream_obj.Icecream_Menu(x)

else:
    print("You chose an unavailable product")
