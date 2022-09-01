#bank account with class definition
class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("welcome to deposit and withdrawal machine!")
    
    def deposit(self):
        amount = float(input("enter amount to be deposited: "))
        self.balance += amount
        print("amount deposit: ", amount) 
    
    def withdraw(self):
        amount = float(input("enter amount to withdraw: "))
        if self.balance>=amount:
            self.balance-=amount
            print("you withdraw: ", amount)
        else:
            print("net available balance=", self.balance)
    
    def display(self):
        print("net available balance=", self.balance)
        
#create object class
Gideon_Account = Bank_Account()

#functions with that class
Gideon_Account.deposit()
Gideon_Account.withdraw()
Gideon_Account.display()