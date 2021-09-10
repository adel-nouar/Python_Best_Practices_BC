"""
Demo of naming and some information about PEP8
www.python.org/dev/peps/pep-0008/
"""
from pygame import init


EUR_USD_EXCHANGE_RATE = 1.20


# Bad examples
var = ... # doesn't mean something useful 
data = ... # don't give something useful about what the value is
temp = ... # It's confusing, it's temperature, temporare ?
df = ... # Doesn't describe what the data is
list = ... # List is also a function, we couldn't use it
print = ... # It a default python function
l = ... # Don't helpful, doesn't mean anything and could be interpreted as number one
distance = ... # In kilometers, Miles, or what ?
fname = ... # Avoid abbreviation when it's possible, use first_name instead


# Good examples
number_of_children = 2
age = 42
postal_code = 94500


# Two words concatenated : using snake case
street_name = "Main Street"


# Function names
def convert(amout): # BAD : The name doesn't tell the purpose of the function
    return amount * 1.20

def convertEur2Usd(amount): # Function name should be lowercase separated by underscore
    return amount * 1.20

def convert_eur_to_usd (amount): # More clear
    return amount * 1.20 # The 1.20 should be a constant, because if we use 1.20 many times, we have to change it everywhere

def convert_eur_to_usd (amount): # Excellent using constant
    return amount * EUR_USD_EXCHANGE_RATE


# Class names (PascalCase)
class RectangleShape:
    def __init__(self, width, length) -> None:
        self.width = width
        self.length = length
    
    def calculate_area(self):
        return self.width * self.length
