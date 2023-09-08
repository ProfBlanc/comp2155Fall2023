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
    
    while total_price < budget:
        name = input("Enter name of article: ")
        description = input(f"Enter description of {name}: ")
        price = float(input(f"The price of {name} is?: "))
        total_price += price
except TypeError:
    print("Invalid budget value")
except ValueError:
    print("Invalid article price value")
