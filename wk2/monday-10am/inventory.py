"""
ask user for a budget
continally ask user for product
    name, description, price
until reached the budget limit
"""
import sys

try:
    answer = input("Enter a budget: ")
    if not answer.isdigit():
        raise TypeError()
    budget = int(answer)
    print(f"My budget is ${budget} dollars")
    amount_of_money_spent = 0
    while amount_of_money_spent < budget:
        name = input("Enter name of product: ")
        description = input("Describe " + name + ": ")
        price = float(input(f"The price of {name} is: "))
        amount_of_money_spent += price
    print(f"You have spent "
          f"${amount_of_money_spent} dollars today")

except TypeError:
    print("Invalid budget value", file=sys.stderr)
except ValueError:
    print("Invalid product price value", file=sys.stderr)
