"""
Benefit of OOP : 
                - Writting clean and clear code
                - Improved productivity (don't repeat yourself DRY)
                - Faster dev
                - Use proven design patterns
                - Easier to test and maintain
Demo classes and instances

"""


# Demo class
class Rectangle: # Always starts with capital letter without underscore with It (Camel case)
    """Represent a rectangle with area calculus"""
    def __init__(self, length:float, width:float ) -> None:
        self.length = length
        self.width = width

    def area(self):
        """Return area of the rectangle"""
        return self.length * self.width

my_object = Rectangle(10, 20)

# Attribute length
print(my_object.length)

# Area
print(my_object.area())


# Demo Bank account
class BankAccount: # Separate word By capital (Camel case)
    """Represent a bank account"""
    def __init__(self, owner:str, balance:float=0) -> None:
        self.owner = owner
        self.balance = balance

    def deposite(self, amount:float):
        """Method used to depose money to the account"""
        self.balance += amount

    def withdraw(self, amount:float):
        """Method used to withdraw money to the account"""
        self.balance -= amount

    def show_balance(self):
        """Method used to show the balance of the account"""
        print(f"{self.owner} has EUR: {self.balance}")


account_john = BankAccount("John")
account_john.deposite(100)
account_john.show_balance()
account_john.withdraw(23)
account_john.show_balance()

account_jessica = BankAccount("Jessica", 500)
account_jessica.show_balance()
account_jessica.deposite(1000)
account_jessica.show_balance()



# Inheritance 
class Base:
    pass


class Derived(Base):
    pass


class Vehicle:
    description = "This is a vehicle"

    def drive(self):
        print("Driving")

    def brake(self):
        print("Braking")
    
class Car(Vehicle):
    wheels = 4

class Truck(Vehicle):
    wheels = 4