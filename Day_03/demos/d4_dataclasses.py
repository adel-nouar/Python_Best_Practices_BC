"""
Demo dataclasses
PEP 557
"""
from dataclasses import dataclass # Since python 3.7

# Example regular class
class RegularClassCustomer:
    """Class to represent a customer."""
    def __init__(self, name:str, email:str, is_active:bool = False) -> None:
        self.name = name
        self.email = email
        self.is_active = is_active




# Examples of two instances
c1 = RegularClassCustomer("John Doe", "John@doe.com")
print(c1)
c2 = RegularClassCustomer("John Doe", "John@doe.com")
print(c2 == c1)

print(f'id c1: {id(c1)}')
print(f'id c2: {id(c2)}')


# Example dataclass
@dataclass
class DataClassCustomer:
    """Class to represent a customer."""
    name: str
    email: str
    is_active: bool = False


# Examples of two instances
d1 = DataClassCustomer("John Doe", "john@doe.com")
print(d1)
d2 = DataClassCustomer("John Doe", "john@doe.com")
print(d1 == d2)