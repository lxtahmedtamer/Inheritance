class VendingMachine:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.selection = 0  # indicator for item selection
        self.money_rest = 0  # indicator for money difference for the client
        print("WELCOME TO THE VENDING MACHINE:")

    def display_menu(self):
        # MENU DISPLAY
        pass

    def select_item(self):
        self.selection = int(input("Choose a number from 1 to 4:"))
        while self.selection < 1 or self.selection > 4:
            self.selection = int(input("Sorry, please enter a valid number from 1 to 4:"))
        else:
            return self.selection

    def payment(self):
        amount = float(input("Please insert money: "))
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount. "))
        
        while amount < self.price:
            amount = float(input(f"Please insert enough money to buy {self.name}: "))
        
        # PROCESS FINISHED
        self.money_rest = amount - self.price
        print("Thank you for using the Vending Machine!")   
        print("Your rest of money =", self.money_rest)

    def last_phase(self):
        self.display_menu()
        self.selection = self.select_item()
        self.payment()


class Product(VendingMachine):
    def __init__(self):
        super().__init__()  # Ensure proper initialization of the parent class
        self.product_selection = ""
        self.cost=0

    def select_product(self):
        Product_list = ["Hot Drink", "Cold Drink", "Snack"]
        print("Products available in Vending Machine are:", Product_list)
        self.product_selection = input("Choose a product from the previous: ")
        while self.product_selection not in Product_list:
            self.product_selection = input("Sorry, please enter a valid choice: ")
        ##else:
           ## return self.product_selection

    def product_price(self,hot_input):
        # Price is unified for each product
        if self.hot_input == "Hot Drink":
            self.cost= 20
        elif self.product_selection == "Cold Drink":
            self.cost= 30
        elif self.product_selection == "Snack":
            self.cost = 40
        print(self.cost)    
        super().payment()


class HotDrink(Product):
    def __init__(self):
        super().__init__()
        self.hot_input=""
    def HotDrink_Menu(self):
        HotDrink_list = ["Tea", "Nescafe", "Hot Chocolate"]
        print("Hot Drinks available are", HotDrink_list)
        self.hot_input = input("Choose a Hot Drink product: ")
        while self.hot_input not in HotDrink_list:
            self.hot_input = input("Sorry, please enter a valid choice: ")
        else:
            return self.hot_input

    def __str__(self):
        return f"{self.name} (Hot) - ${self.price:.2f}"


class ColdDrink(Product):
    def __init__(self):
        super().__init__()

    def ColdDrink_Menu(self):
        ColdDrink_list = ["Pepsi", "Seven up", "Mirinda"]
        print("Cold Drinks available are", ColdDrink_list)
        self.name = input("Choose a Cold Drink product: ")
        while self.name not in ColdDrink_list:
            self.name = input("Sorry, please enter a valid choice: ")
        else:
            pass

    def __str__(self):
        return f"{self.name} (Cold) - ${self.price:.2f}"


class Snack(Product):
    def __init__(self):
        super().__init__()

    def Snack_Menu(self):
        Snack_list = ["Chipsy", "Cheetos", "Doritos"]
        print("Snacks available are", Snack_list)
        self.name = input("Choose a Snack product: ")
        while self.name not in Snack_list:
            self.name = input("Sorry, please enter a valid choice: ")
        else:
            pass

    def __str__(self):
        return f"{self.name} (Snack) - ${self.price:.2f}"


obj=Product()
obj.select_product()
if obj.product_selection=="Hot Drink":
    hot_obj = HotDrink()
    hot_obj.HotDrink_Menu()
    hot_obj.product_price(obj.product_selection)
    
elif y == "Cold Drink":
    cold_obj = ColdDrink()
    cold_obj.ColdDrink_Menu()
    cold_obj.product_price()
   
elif y == "Snack":
    snack_obj = Snack()
    snack_obj.Snack_Menu()
    snack_obj.product_price()
   
else:
    print("You chose an unavailable product")
