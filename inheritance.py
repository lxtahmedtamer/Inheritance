"""
In the following code Concept of Inheritance is applied by creating a child(Coffee Vending Machine) to the parent class(Vending Machine)
and adding more facilities in buying coffee
"""

class VendingMachine:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.selection = 0  # indicator for item selection
        self.money_rest = 0  # indicator for money difference for the client
        print("WELCOME TO THE VENDING MACHINE:")

    def display_menu(self):
        # MENU DISPLAY
        #print("The Menu is as the following:")
        self.items = {
            1: {'name': 'Item1', 'price': 20},
            2: {'name': 'Item2', 'price': 30},
            3: {'name': 'Item3', 'price': 35},
            4: {'name': 'Item4', 'price': 40}
        }

        """
        for key, value in self.items.items():
            print(f"{key}: {value['name']} - {value['price']}")
        """
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
        
        item_price = self.items[self.selection]['price']
        while amount < item_price:
            amount = float(input(f"Please insert enough money to buy {self.items[self.selection]['name']}: "))
        
        # PROCESS FINISHED
        self.money_rest = amount - item_price
        print("Thank you for using the Vending Machine!")   
        print("Your rest of money =", self.money_rest)


    def last_phase(self):
        self.display_menu()
        self.selection = self.select_item()
        self.payment()
    


class Coffee_VendingMachine(VendingMachine):
    def __init__(self):
        super().__init__()
        print("Welcome to the Coffee Vending Machine:")
        
    def display_coffee_menu(self):
        super().display_menu()
        #  Coffee MENU DISPLAY
        print("The Menu is as the following:")
        self.coffee_drinks = {
            1: {'name': 'Nescafe', 'price': 20},
            2: {'name': 'Latte', 'price': 30},
            3: {'name': 'Cappuccino', 'price': 35},
            4: {'name': 'Mocha', 'price': 40}
        }

        for key, value in self.coffee_drinks.items():
            print(f"{key}: {value['name']} - {value['price']}")
    
    def Extra_Options(self):
        Size=["Large","Medium","Small"]
        Flavors_Additions=["Vanilla","Caramel","Hazelnut"]
        Sugar_Level=["Extra Sugar","Sugar adjusted","No sugar"]
         
        print("Size Options are",Size)
        size_input=input("Choose Size:")
        while(size_input not in Size): 
            print("Please Enter a Correct Option , Where please type answer with same alphebatic form shown:")
            size_input=input("Choose Size:")
            if(size_input in Size):
                break
        
        
        print("Extra Flavors are",Flavors_Additions)
        Flavors_input=input("Choose Extra Flavors:")
        while(Flavors_input not in Flavors_Additions): 
            print("Please Enter a Correct Option , Where please type answer with same alphebatic form shown:")
            Flavors_input=input("Choose Extra Flavors:")
            if(Flavors_input in Flavors_Additions):
                break
        
        print("Extra Flavors are",Sugar_Level)
        sugar_input=input("Choose Sugar input:")
        while(sugar_input not in Sugar_Level): 
            print("Please Enter a Correct Option , Where please type answer with same alphebatic form shown:")
            sugar_input=input("Choose Sugar input:")
            if(sugar_input in Sugar_Level):
                break


# Creating an instance for the Coffee Vending Machine class    
obj=Coffee_VendingMachine()  #An instance of child class
obj.display_coffee_menu()
obj.select_item()
obj.Extra_Options()
obj.payment()

print("Enjoy Your Coffee drink")

      



