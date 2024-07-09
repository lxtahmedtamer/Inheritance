""" 
This Code shows the concept of Abstraction as defining a layout for any Vending Machine created later
"""
from abc import ABC, abstractmethod

class AbstractVendingMachine(ABC):
    def __init__(self):
        self.name: str
        self.price: float
        self.selection: int
        self.money_rest: float

    @abstractmethod
    def display_menu(self):
        pass

    @abstractmethod
    def select_item(self):
        pass

    @abstractmethod
    def payment(self):
        pass

    def last_phase(self):
        pass

class VendingMachine(AbstractVendingMachine):
    def __init__(self):
        # Initilization for values of variables
        self.name = ""
        self.price = 0
        self.selection = 0  # indicator for item selection
        self.money_rest = 0  # indicator for money difference for the client
        
        self.items = {
            1: {'name': 'Item1', 'price': 20},
            2: {'name': 'Item2', 'price': 30},
            3: {'name': 'Item3', 'price': 35},
            4: {'name': 'Item4', 'price': 40}
        }
        print("WELCOME TO THE VENDING MACHINE:")
    def display_menu(self):
        print("The Menu is as follows:")
        for key, value in self.items.items():
            print(f"{key}: {value['name']} - {value['price']}")

    def select_item(self):
        self.selection = int(input("Choose a number from 1 to 4: "))
        while self.selection < 1 or self.selection > 4:
            self.selection = int(input("Sorry, please enter a valid number from 1 to 4: "))
        return self.selection

    def payment(self):
        amount = float(input("Please insert money: "))
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount: "))
        
        item = self.items.get(self.selection)
        if item is None:
            print("Invalid selection.")
            return
        
        item_price = item['price']
        while amount < item_price:
            amount = float(input(f"Please insert enough money to buy {item['name']}: "))
        
        self.money_rest = amount - item_price
        print("Thank you for using the Vending Machine!")   
        print("Your change is:", self.money_rest)
    
    
    def last_phase(self):
        self.display_menu()
        self.selection = self.select_item()
        self.payment()

# Main Function
vm = VendingMachine()
vm.last_phase()

