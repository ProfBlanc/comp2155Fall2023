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
    purchases = list()
    while amount_of_money_spent < budget:
        name = input("Enter name of product: ")
        description = input("Describe " + name + ": ")
        price = float(input(f"The price of {name} is: "))
        if amount_of_money_spent + price > budget:
            print(f"Cannot buy {name} because it is "
                  f"${(amount_of_money_spent + price ) - budget}"
                  f" over the budget. "
                  "Please buy something that cost no more than "
                  f"${budget - amount_of_money_spent} dollars")
            continue  # break to stop the spending
        amount_of_money_spent += price
        purchases.append({"name": name, "description": description,
                          "price": price})
    print(f"You have purchased {len(purchases)} items. You have spent "
          f"${amount_of_money_spent} dollars today")

    file = open("receipt.txt", "w")
    file.write("Store Receipt\n\n")
    file.write("Name " + '\t' * 4 + "Description" + '\t' * 8 + "Price" + '\n')
    for item in purchases:
        file.write(item['name'] + "\t" * 4 + item['description']
                   + "\t" * 8 + str(item['price']) + "\n")
    file.write("Total" + '\t' * 12 + str(amount_of_money_spent))
except TypeError:
    print("Invalid budget value", file=sys.stderr)
except ValueError:
    print("Invalid product price value", file=sys.stderr)
