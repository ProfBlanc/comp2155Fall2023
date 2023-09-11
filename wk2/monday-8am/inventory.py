"""
ask the user for a budget
continually ask user for
    product name
    description
    price
until budget is reached or exceeded
"""
import sys

try:
    user_text = input("Enter a budget: ")
    if not user_text.isdigit():
        raise TypeError()
    budget = int(user_text)
    print(f"My budget is ${budget} CAD")

    total_price = 0
    # total_items = 0
    summary = list()
    while total_price < budget:
        name = input("Enter product name: ")
        description = input(f"Enter {name} description: ")
        price = float(input(f"Enter {name} price: "))
        if total_price + price > budget:
            print(f"{name} cannot be purchase because it is "
                  f"${(total_price + price) - budget} dollars over the budget.")
            break
        summary.append({"name": name,
                        "price": price, "description": description})
        # total_items += 1
        total_price += price
    # print(f"You purchase {total_items} and spent ${total_price} dollars")
    print(f"You purchase {len(summary)} and spent ${total_price} dollars")

    print("Store Receipt", file=open("receipt.txt", "a"))
    for item in summary:
        print(f"Name: {item['name']}, Description: {item['description']}"
              f", Price: {item['price']}", file=open('receipt.txt', 'a'))

    print(f"Grand total = {total_price}", file=open("receipt.txt", "a"))
    print("*" * 20, file=open("receipt.txt", "a"))
except TypeError:
    print("Invalid budget value", file=sys.stderr)
except ValueError:
    print("Invalid product price value", file=sys.stderr)
