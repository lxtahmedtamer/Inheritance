""" 
This Code shows the concept of Abstraction as defining a layout for any Vending Machine created later
"""
from abc import ABC, abstractmethod

class AbstractVendingMachine(ABC):
    
   

    @abstractmethod
    def set_amount(self, amount):
        pass

    @abstractmethod
    def get_amount(self):
        pass

    @abstractmethod
    def set_selection(self, amount):
        pass

    @abstractmethod
    def get_selection(self):
        pass

    @abstractmethod
    def display_menu(self):
        pass

  

    @abstractmethod
    def payment(self):
        pass

    


        
        
class VendingMachine(AbstractVendingMachine):
   
    def set_amount(self, amount):
        self.selection:float
        self.amount=amount

    
    def get_amount(self):
        return self.amount

    def set_selection(self, select):
        self.selection:int 
        self.selection=select

    
    def get_selection(self):
        return self.selection   

    def display_menu(self):
        # changing the dict to this
        self.Products_List = ["product1","product2","product3","product4"]
        self.Prices_List=[30,40,50,60]
        print("The Menu is as follows:")
        
        for i in range(len(self.Products_List)):
            print(f"{self.Products_List[i]}: ${self.Prices_List[i]}")
        

    def Selecting_Product(self,select):
        
        self.selection = select
        while self.selection < 1 or self.selection > 4:
            self.set_selection( int(input("Sorry, Please enter a valid number from 1 to 4: ")))
            self.selection=self.get_selection()
        if self.selection==1:
            #Product1
            self.price=self.Prices_List[0]
            
        elif self.selection==2:
            #Product2
            self.price=self.Prices_List[1]
        elif self.selection==3:
            #Product3
            self.price=self.Prices_List[2]
        elif self.selection==4:
            #Product4
            self.price=self.Prices_List[3]       
        
        return self.selection

    def payment(self,pay):
        amount=pay
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount: "))
        while amount < self.price:
            amount = float(input(f"Please insert enough money to buy {self.Products_List[self.selection-1]}: "))
        
        self.money_rest = amount - self.price
        print("Thank you for using the Vending Machine!")   
        print("Your change is:", self.money_rest)
    
    
    
# Main Function
vm = VendingMachine()
vm.display_menu()
vm.set_selection(4)
selected_number=vm.get_selection()
vm.Selecting_Product(selected_number)
vm.set_amount(100.5)
budget=vm.get_amount()  # Correct usage of get_amount() method
vm.payment(budget)

