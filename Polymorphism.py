class VM:
    def __init__(self):
        self.name = ""
        self.price = 0
        self.x = 0  # indicator for coffee type
        self.money_rest = 0  # indicator for money difference for the client
        print("WELCOME TO THE  VENDING MACHINE:")
       
    def display_menu(self):
        # MENU DISPLAY
        print("The Menu is as the following:")
        self.drinks = {
            1: {'name': 'Drink1', 'price': 20},
            2: {'name': 'Drink2', 'price': 30},
            3: {'name': 'Drink3', 'price': 35},
            4: {'name': 'Drink4', 'price': 40}
        }
    
        for key, value in self.drinks.items():
            print(f"{key}: {value['name']} - {value['price']}")
            
            
    def select_drink(self):
        self.x = int(input("Choose a number from 1 to 4:"))
        while self.x < 1 or self.x > 4:
            self.x = int(input("Sorry, Please Enter a Valid number from 1 to 4:"))
        
        return self.x

    def payment(self):
        amount = float(input("Please insert money: "))
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount. "))
            
        if self.x == 1:
            self.price = 20
            while amount < 20:
                 amount = float(input("Please insert money applicable to buy Nescafe: "))
        elif self.x == 2:
            self.price = 30
            while amount < 30:
                 amount = float(input("Please insert money applicable to buy Latte: "))
        elif self.x == 3:
            self.price = 35  
            while amount < 35:
                 amount = float(input("Please insert money applicable to buy Cappuccino: "))      
        elif self.x == 4:
            self.price = 40
            while amount < 40:
                 amount = float(input("Please insert money applicable to buy Mocha: "))
        
        # PROCESS FINISHED                
        self.money_rest = amount - self.price
        print("Thank you for using the Vending Machine!")   
        print("Your rest of money =", self.money_rest)
    
    def last_phase(self):
        self.display_menu()
        self.x = self.select_drink()
        self.payment()


class NewVendingMachine(VM):
    def payment(self):
        amount = float(input("Please insert money: "))
        while amount <= 0:
            amount = float(input("Invalid amount. Please insert a positive amount. "))
            
        if self.x == 1:
            self.price = 50
            while amount < 50:
                 amount = float(input("Please insert money applicable to buy Special Nescafe: "))
        elif self.x == 2:
            self.price = 60
            while amount < 60:
                 amount = float(input("Please insert money applicable to buy Special Latte: "))
        elif self.x == 3:
            self.price = 70  
            while amount < 70:
                 amount = float(input("Please insert money applicable to buy Special Cappuccino: "))      
        elif self.x == 4:
            self.price = 80
            while amount < 80:
                 amount = float(input("Please insert money applicable to buy Special Mocha: "))
        
        # PROCESS FINISHED                
        self.money_rest = amount - self.price
        print("Thank you for using the Custom Vending Machine!")   
        print("Your rest of money =", self.money_rest)


# Creating an instance of CustomVM
vending_machine = NewVendingMachine()
vending_machine.last_phase()
