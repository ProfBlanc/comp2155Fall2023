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


def must_be_at_least_3_chars(text):
    return len(text) > 2


def validate_price(price):
    text = str(price)
    if "." not in text:
        return True
    else:
        return not len(text) > text.index(".") + 2


try:
    user_text = input("Enter a budget: ")

    if not user_text.isdigit():
        raise TypeError("Budget is invalid")

    budget = float(user_text)

    total_cost = 0
    number_of_articles = 0
    summary = list()
    while total_cost <= budget:
        name = input("Enter name of article: ")
        description = input(f"Enter description of {name}: ")

        # if must_be_at_least_3_chars(name) and must_be_at_least_3_chars(description):
        #     pass
        # else:
        #     raise NameError()
        if not must_be_at_least_3_chars(name) or not must_be_at_least_3_chars(description):
            raise NameError()
        price = float(input("Enter price of " + name + ": "))

        if not validate_price(price):
            raise ArithmeticError()

        if price + total_cost > budget:
            print(f"Sorry but {name} cost too much. This will "
                  f"bring us ${(price + total_cost) - budget} over our budget")
            break

        number_of_articles += 1
        total_cost += price
        summary.append({"name": name, "description": description, "price": price})
        print("Good job! Moving on to next article")

    print(f"Number of articles = {number_of_articles}, "
          f"total price = {total_cost}")

    f = open("receipt.txt", "w")
    f.write("Our Awesome Store\n\n")
    f.write("Name" + "\t" * 8 + "Description" + "\t" * 8 + "Price" + "\n")
    for item in summary:
        f.write(item['name'] + "\t" * 8 + item['description'] + "\t" * 8 + str(item['price']) + "\n")
    f.write("Total" + '\t' * 18 + str(total_cost))
except TypeError as e:
    print(f"Invalid budget value of {user_text}", file=sys.stderr)
except NameError as e:
    print(f"Name and or description is invalid", file=sys.stderr)
except ArithmeticError as e:
    print(f"Price has too many significant digits", file=sys.stderr)
except ValueError as e:
    # print(f"Invalid budget value of {user_text}", file=sys.stderr)
    print(f"Invalid article price", file=sys.stderr)
