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
    def select_product(self, y):
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

    def select_product(self, y):
        Product_list = ["Hot Drink", "Cold Drink", "Snack", "Ice Cream"]
        #print("Products available in Vending Machine are:", Product_list)
        while y not in Product_list:
            y = input("Please Enter your Product Cateogry again ")
        return y

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

    def product_payment(self):
        budget = self.get_amount()  # Get amount as float
        while budget <= 0:
            budget = float(input("Invalid amount. Please insert a positive amount: "))
        
        while budget < self.cost:
            budget = float(input(f"Please insert enough money to buy {self.product_selection}: "))
        
        self.money_rest = budget - self.cost
        print("Thank you for using the Vending Machine!")   
        print("Your remaining money =", self.money_rest)   

class HotDrink(Product):
    def HotDrink_Menu(self):
        HotDrink_list = ["Tea", "Nescafe", "Hot Chocolate"]
        print("Hot Drinks available are", HotDrink_list)
        self.product_selection = self.select_product(input("Choose a Hot Drink product: "))
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment()

class ColdDrink(Product):
    
   
    def ColdDrink_Menu(self):
        ColdDrink_list = ["Pepsi", "Seven up", "Mirinda"]
        print("Cold Drinks available are", ColdDrink_list)
        self.product_selection = self.select_product(input("Choose a Cold Drink product: "))
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment()

class Snack(Product):
    
    
    def Snack_Menu(self):
        Snack_list = ["Chipsy", "Cheetos", "Doritos"]
        print("Snacks available are", Snack_list)
        self.product_selection = self.select_product(input("Choose a Snack product: "))
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment()

class Icecream(Product):
    
    def Icecream_Menu(self):
        Icecream_list = ["Chocolate", "Vanilla", "Strawberry"]
        print("Ice Cream Flavors available are", Icecream_list)
        self.product_selection = self.select_product(input("Choose an Ice Cream flavor: "))
        self.product_price()
        self.set_amount(input("Please enter the money you own: "))
        self.product_payment()

# Main Product selection
obj = Product()
obj.set_product_name("Cold Drink")

if obj.get_product_name() == "Hot Drink":
    hot_obj = HotDrink()
    hot_obj.HotDrink_Menu()
    
elif obj.get_product_name() == "Cold Drink":
    cold_obj = ColdDrink()
    cold_obj.ColdDrink_Menu()
    
elif obj.get_product_name() == "Snack":
    snack_obj = Snack()
    snack_obj.Snack_Menu()

elif obj.get_product_name() == "Ice Cream":
    icecream_obj = Icecream()
    icecream_obj.Icecream_Menu()

else:
    print("You chose an unavailable product")
