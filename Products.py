
class Product:
    def __init__(self):
        self.product_selection = ""
        self.cost = 0
        self.amount=0
        self.money_rest=0

    def select_product(self):
        Product_list = ["Hot Drink", "Cold Drink", "Snack"]
        print("Products available in Vending Machine are:", Product_list)
        self.product_selection = input("Choose a product from the previous: ")
        while self.product_selection not in Product_list:
            self.product_selection = input("Sorry, please enter a valid choice: ")
        return self.product_selection

    def product_price(self):
        # Price is unified for each product
        if self.product_selection == "Hot Drink":
            self.cost = 20
        elif self.product_selection == "Cold Drink":
            self.cost = 30
        elif self.product_selection == "Snack":
            self.cost = 40
        print(f"Price for {self.product_selection}: ${self.cost}")    

    def product_payment(self):
        self.amount = float(input("Please insert money: "))
        while self.amount <= 0:
            self.amount = float(input("Invalid self.amount. Please insert a positive self.amount. "))
        
        while self.amount < self.cost:
            self.amount = float(input(f"Please insert enough money to buy {self.input_type}: "))
        
        # PROCESS FINISHED
        self.money_rest = self.amount - self.cost
        print("Thank you for using the Vending Machine!")   
        print("Your rest of money =", self.money_rest)   

class HotDrink(Product):
    def __init__(self):
        super().__init__()
        self.input_type = ""

    def HotDrink_Menu(self):
        HotDrink_list = ["Tea", "Nescafe", "Hot Chocolate"]
        print("Hot Drinks available are", HotDrink_list)
        self.input_type = input("Choose a Hot Drink product: ")
        while self.input_type not in HotDrink_list:
            self.input_type = input("Sorry, please enter a valid choice: ")
        return self.input_type

    


class ColdDrink(Product):
    def __init__(self):
        super().__init__()
        self.input_type = ""

    def ColdDrink_Menu(self):
        ColdDrink_list = ["Pepsi", "Seven up", "Mirinda"]
        print("Cold Drinks available are", ColdDrink_list)
        self.input_type = input("Choose a Cold Drink product: ")
        while self.input_type not in ColdDrink_list:
            self.input_type = input("Sorry, please enter a valid choice: ")



class Snack(Product):
    def __init__(self):
        super().__init__()
        self.input_type = ""

    def Snack_Menu(self):
        Snack_list = ["Chipsy", "Cheetos", "Doritos"]
        print("Snacks available are", Snack_list)
        self.input_type = input("Choose a Snack product: ")
        while self.input_type not in Snack_list:
            self.input_type = input("Sorry, please enter a valid choice: ")

    


obj = Product()
choice = obj.select_product()
if choice == "Hot Drink":
    hot_obj = HotDrink()
    hot_obj.HotDrink_Menu()
    hot_obj.product_selection = choice
    hot_obj.product_price()
    hot_obj.product_payment()
    
elif choice == "Cold Drink":
    cold_obj = ColdDrink()
    cold_obj.ColdDrink_Menu()
    cold_obj.product_selection = choice
    cold_obj.product_price()
    cold_obj.product_payment()
    
elif choice == "Snack":
    snack_obj = Snack()
    snack_obj.Snack_Menu()
    snack_obj.product_selection = choice
    snack_obj.product_price()
    snack_obj.product_payment()
    
else:
    print("You chose an unavailable product")
