"""
Exercise
Add type hints to the code below and catch the bug.
"""


def main() -> None:
    """Simple program for illustrative purposes"""
    age:int = ask_user_age()
    print_age(age)


def ask_user_age() -> int:
    """Return user input"""
    age = int(input("What is your age in years? "))
    return age


def print_age(age:int) -> None:
    """Print full sentence"""
    age_in_months:int = age * 12
    print(f"You are {age_in_months} months old.")


if __name__ == "__main__":
    main()
