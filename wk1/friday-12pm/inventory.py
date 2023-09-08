"""
Ask user for a budget
    Continually ask user until budget is reached
            name of article
            description of article
            price of article

    *When are we going to stop?
        When sum of article prices is equal or surpasses budget
"""
import sys
budget = ""
user_text = ""
try:
    user_text = input("Enter a budget: ")

    if not user_text.isdigit():
        raise TypeError("Budget is invalid")

    budget = float(user_text)

    total_cost = 0
    number_of_articles = 0
    while total_cost <= budget:
        name = input("Enter name of article: ")
        description = input(f"Enter description of {name}: ")
        price = float(input("Enter price of " + name + ": "))
        if price + total_cost > budget:
            print(f"Sorry but {name} cost too much. This will "
                  f"bring us ${(price + total_cost) - budget} over our budget")
            break

        number_of_articles += 1
        total_cost += price
        print("Good job! Moving on to next article")
    print(f"Number of articles = {number_of_articles}, "
          f"total price = {total_cost}")
except TypeError as e:
    print(f"Invalid budget value of {user_text}", file=sys.stderr)

except ValueError as e:
    # print(f"Invalid budget value of {user_text}", file=sys.stderr)
    print(f"Invalid article price", file=sys.stderr)
