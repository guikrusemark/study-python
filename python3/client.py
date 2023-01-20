from typing import List
import account


class Client:
    name: str
    cpf: str
    address: str = "Address not registered"
    accounts: List[account.Account] = []

    def __init__(self, name: str, cpf: str, accounts: List[account.Account]):
        self.name: str = name
        self.cpf: str = cpf
        self.accounts: List[account.Account] = accounts

    @property
    def __str__(self):
        return f"Name: {self.name}\nCPF: {self.cpf}\nAddress: {self.address}\nAccounts: {self.accounts}"
