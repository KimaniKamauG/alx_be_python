class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance
    
    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance < amount:
            return "Insufficient funds!"
        else:
            self.account_balance -= amount
            return self.account_balance
        
    def display_balance(self):
        return f"Your current balance is ${self.account_balance}. Thank you for your service."
    
