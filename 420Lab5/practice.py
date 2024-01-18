

class BankAccount:

    def __init__(self,owner,balance= 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance = self.balance - amount
        else: 
            print("cannot withdraw")
    def get_balance(self):
        return self.balance
    