"""
Inventory script
Ask user for a budget
Continually ask user for article
    name, description, price
stop asking when we have reached budget limit
Output how many articles and total price of purchase
"""
import re
import sys


def validate_text(text, min_chars):
    return len(text) >= min_chars


def validate_price(price):
    text = str(price)
    return re.match(pattern=r"[+-]?\d+\.\d{3,}", string=text)



try:
    answer = input("Enter a budget: ")
    if not answer.isdigit():
        raise TypeError()

    budget = int(answer)

    print(f"Your budget is ${budget}")
    total = 0
    num_items = 0
    summary = list()
    while total < budget:
        name = input("Enter name of article: ")
        description = input(f"Describe {name}: ")

        if not validate_text(name, 3) or not validate_text(min_chars=3, text=description):
            raise NameError()

        price = float(input(f"Enter price of {name}: "))

        if validate_price(price):
            raise IndexError()

        if price + total > budget:
            print(f"Cannot add {name} to shopping cart. "
                  f"Why? Because you are "
                  f"${(total + price) - budget} over budget")
            print(f"You only have ${budget - total} remaining in the budget")
            print("Please try again")
        else:
            num_items += 1
            total += price
            summary.append({"name": name, "description": description, "price": str(price)})

    print(f"You entered {num_items} items. The total is {total}. "
          f"{round(total * 1.13, 2)} with tax. ")

    f = open("receipt.txt", "w")
    f.write("Our Store Receipt\n\n")
    f.write("Name" + '\t' * 8 + "Description" + '\t' * 8 + "Price" + '\n')
    for item in summary:
        f.write(item['name'] + "\t" * 8 + item['description'] + '\t' * 8 + item['price'] + "\n")

    f.write("\nTotal = " + '\t' * 18 + str(total))

except IndexError:
    print("Price has too many decimals", file=sys.stderr)
except TypeError:
    print("Invalid budget value", file=sys.stderr)
except NameError:
    print("Invalid article name and/or description", file=sys.stderr)
except ValueError:
    print("Invalid article price", file=sys.stderr)
