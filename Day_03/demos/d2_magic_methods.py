"""
Demo magic methods. Run file instead of using console.
"""
from functools import total_ordering

@total_ordering # Used to compare classes instead of defining each __eq__, __gt__, etc...
class BankAccount:

    def __init__(self, owner:str, balance:float=0) -> None:
        self.owner = owner
        self.balance = balance
    
    def __eq__(self, other) -> bool:
        return self.balance == other.balance

    def __gt__(self, other) -> bool:
        return self.balance > other.balance
    
    def __str__(self) -> str:
        return f"Bank account of {self.owner}"

    def __repr__(self) -> str: # Mainly used for developper, but if we don't implement __str__ it'll use __repr__ for printing the object
        return f'BankAccount("{self.owner}")'


account_john = BankAccount("John", 100)
print(account_john)
account_jane = BankAccount("Jane", 100)

print(account_john > account_jane)
print(account_john == account_jane)
print(account_john <= account_jane)

