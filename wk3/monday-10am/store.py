import csv
import os.path
import sys

base_dir = "data"
class Product:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.save()
    def __str__(self):
        return f"Barcode = {self.barcode}, " \
               f"Name = {self.name}, Price = {self.price}"
    def save(self):
        if not os.path.exists(base_dir):
            os.mkdir(base_dir)
        f = open(base_dir + "/" + self.barcode, "w")
        f.write(f"{self.name}\n{self.price}")
def get_product(barcode):
    if barcode in os.listdir(base_dir):
        with open(base_dir + "/" + barcode) as file:
            content = file.readlines()
            name = content[0].strip()
            price = float(content[1].strip())
            return Product(barcode=barcode,
                           name = name,
                           price=price)

def buy():
    print("Welcome, Customer!")
    summary = list()
    while True:
        answer = input("Enter a barcode or (Q)uit to stop").lower()
        if answer[0] == "q":
            print("Thank you for your business")
            break
        product = get_product(answer)
        if product:
            print(f"You have purchase product {product.name} "
                  f"with price {product.price}")
            summary.append({"name": product.name,
                            "price": product.price,
                            "barcode": product.barcode})
        else:
            print(f"Product with barcode {answer} does not exists")

    print(f"You purchases {len(summary)} items. "
          f"The total price is { sum([ item['price'] for item in summary]) }")

    with open("receipt.csv", "w") as file:
        writer = csv.DictWriter(file, lineterminator='\n', quotechar="'",delimiter=',' ,fieldnames=vars(Product("a", "b", "c")))
        writer.writeheader()
        writer.writerows(summary)


def manage():
    print("Welcome Store Owner")
    print("You will enter product details")
    # barcode, name, price
    try:
        barcode = input("Enter barcode: ")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        if barcode in os.listdir(base_dir):
            raise TypeError()
        Product(barcode=barcode, name=name, price=price)
    except TypeError:
        print(f"Sorry but barcode {barcode} already exists")
    except ValueError:
        print("Invalid price", file=sys.stderr)
def main():
    print("Welcome to our Store")
    choice = input("Do you want to BUY or MANAGE?").lower().strip()
    if choice in ["buy", "manage"]:
        if choice == "buy":
            buy()
        elif choice == "manage":
            manage()
    else:
        print("Invalid option chosen", file=sys.stderr)
if __name__ == '__main__':
    main()
