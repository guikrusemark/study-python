from typing import Dict

class Account:
    __id : int # Private attributes
    __balance : float # Private attributes
    __limit : float = 1000.0 # Static attribute
    
    def __init__(self, id : int, balance : float) -> None: # Constructor
        self.__id : int = id
        self.__balance : float = balance
        
    def withdraw(self, value : float) -> None:
        self.__balance -= value
        
    def deposit(self, value : float) -> None:
        self.__balance += value
        
    def transfer(self, value : float, destiny : "Account") -> None: # "Account" is a string to avoid circular import
        self.withdraw(value)
        destiny.deposit(value)
        
    @property
    @staticmethod
    def limit() -> float: 
        return Account.__limit
    
    @staticmethod
    def account_types() -> Dict[int, str]: 
        return {1 : "Checking", 2 : "Saving", 3 : "Investment"}
            
    def __str__(self) -> str: # String representation
        return f"Account: {self.__id}, Balance: {self.__balance}"