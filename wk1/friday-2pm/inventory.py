"""
Ask user for a budget
Continually ask user for
    name
    description 
    price 
    
    of an article, until they have met exceeded their budget
"""
# welcome user
print("Welcome to our Shopping App")
try:
    # ask user for a budget
    answer = input("What is your budget: ")
    if not answer.isdigit():
        raise TypeError()
    budget = int(answer)
    print(f"Your budget is ${budget}")
    
    total_price = 0
    number_of_items = 0
    
    while total_price < budget:
        name = input("Enter name of article: ")
        description = input(f"Enter description of {name}: ")
        price = float(input(f"The price of {name} is?: "))
        if price + total_price > budget:
            print("Cannot add item. Cannot exceed budget.")
            print(f"You only have ${budget - total_price}. Remaining in budget. Please try again.")
            continue
        number_of_items += 1
        total_price += price
        print(f"{name} added to shopping cart.")
    print(f"You bought {number_of_items} for a total of ${total_price}")    
except TypeError:
    print("Invalid budget value")
except ValueError:
    print("Invalid article price value")
