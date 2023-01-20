

class Account:
    id : int
    balance : float
    limit : float = 1000.0
    
    def __init__(self, id : int, balance : float):
        self.id : int = id
        self.balance : float = balance
        
    def deposit(self, value : float):
        self.balance += value
        
    def withdraw(self, value : float):
        self.balance -= value
        
    def transfer(self, value : float, destiny : "Account"):
        self.withdraw(value)
        destiny.deposit(value)
        
    def __str__(self):
        return f"Account: {self.id}, Balance: {self.balance}"