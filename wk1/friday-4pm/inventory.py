"""
Inventory script
Ask user for a budget
Continually ask user for article
    name, description, price
stop asking when we have reached budget limit
Output how many articles and total price of purchase
"""
import sys

try:
    answer = input("Enter a budget: ")
    if not answer.isdigit():
        raise TypeError()

    budget = int(answer)

    print(f"Your budget is ${budget}")
    total = 0
    num_items = 0
    while total < budget:
        name = input("Enter name of article: ")
        description = input(f"Describe {name}: ")
        price = float(input(f"Enter price of {name}: "))

        if price + total > budget:
            print(f"Cannot add {name} to shopping cart. "
                  f"Why? Because you are "
                  f"${(total + price) - budget} over budget")
            print(f"You only have ${budget - total} remaining in the budget")
            print("Please try again")
        else:
            num_items += 1
            total += price
    print(f"You entered {num_items} items. The total is {total}. "
          f"{round(total * 1.13, 2)} with tax. ")
except TypeError:
    print("Invalid budget value", file=sys.stderr)
except ValueError:
    print("Invalid article price", file=sys.stderr)
