"""
Ask user for a budget
Continually ask user for
    name
    description 
    price 
    
    of an article, until they have met exceeded their budget
"""


def validate_length(text, length):
    return len(text) >= length


def validate_price(price):
    text = str(price)
    return "." in text and len(text) <= text.index(".") + 2

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
    summary = list()
    
    while total_price < budget:
        name = input("Enter name of article: ")
        description = input(f"Enter description of {name}: ")
        
        if not validate_length(name, 3) or not validate_length(description,3):
                raise NameError()
        
        price = float(input(f"The price of {name} is?: "))
        
        if not validate_price(price):
            raise IndexError()
        
        if price + total_price > budget:
            print("Cannot add item. Cannot exceed budget.")
            print(f"You only have ${budget - total_price}. Remaining in budget. Please try again.")
            continue
        number_of_items += 1
        total_price += price
        
        summary.append({"name": name, "price": str(price), "description": description})
        
        print(f"{name} added to shopping cart.")
    print(f"You bought {number_of_items} for a total of ${total_price}")   
    
    f = open("receipt.txt", "w")
    f.write("Shopping Store\n\n")
    f.write("Name" + "\t" * 8 + "Description" + "\t" * 8 + "Price\n" )
    for item in summary:
        f.write(item['name'] + "\t" * 8 + item['description'] + "\t" * 8 + item['price'])
    
except IndexError:
    print("Invalid price")
except NameError:
    print("Invalid name or description. Must be at least 3 characters")
except TypeError:
    print("Invalid budget value")
except ValueError:
    print("Invalid article price value")
