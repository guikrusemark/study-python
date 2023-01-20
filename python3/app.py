from client import Client
from account import Account

client1: Client = Client("John", "123.456.789-00", [Account(1, 1000.0), Account(2, 2000.0), Account(3, 3000.0)])
client1.accounts[0].transfer(100.0, client1.accounts[1])

if __name__ == "__main__":
    for(value) in client1.__dict__.items():
        if value[0] != "accounts":
            print(value)
        else:
            for(account) in value[1]:
                print(account)
