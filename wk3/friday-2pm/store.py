"""
Create a module where Store Owner and Consumer can MANAGE and
BUY products
    barcode, name, price
Store Owner
    add products
        create a text file barcode.txt in a folder
            file contents => product name and price
Consumer
    scan a barcode => retrieve the product info => add to cart

"""
import os.path
import sys


class Product:
    base_dir = "data"
    def __init__(self, barcode, name, price):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.ensure_folder_exists()
        self.save_product()

    def save_product(self):
        f = open(Product.base_dir + "/" + self.barcode + ".txt",
                 "w")
        f.write(f"{self.name}\n{self.price}")
        f.close()
    def ensure_folder_exists(self):
        if not os.path.exists(Product.base_dir):
            os.mkdir(Product.base_dir)
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name if len(name) > 2 else "water"
    @property
    def barcode(self):
        return self.__barcode
    @barcode.setter
    def barcode(self, barcode):
        self.__barcode = barcode

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price):
        if not price.isdigit():
            raise ValueError("Price must be whole number")
        self.__price = int(price)
    @staticmethod
    def does_barcode_exist(barcode):
        return os.path.exists(Product.base_dir + "/" + barcode + ".txt")
    @classmethod
    def get_product_by_barcode(cls, barcode):
        f = open(Product.base_dir + "/" + barcode + ".txt")
        content = f.readlines()
        return cls(barcode=barcode,
                   price=content[1].strip(),
                   name=content[0].strip())
def manage():
    print("You will not by inputting products")
    while True:
        barcode = input("Enter barcode of product: ")
        name = input("Enter name of product: ")
        price = input("Enter price of product: ")
        try:
            p = Product(name=name, price=price, barcode=barcode)
        except ValueError as e:
            print(e, file=sys.stderr)

        answer = input("Do you want to enter another product? "
                       "y/n: ").lower()
        if answer[0] != "y":
            break
    main()
def buy():
    print("You will be buying products")
    summary = list()
    while True:
        answer = input("Enter a barcode or (Q) to stop")
        if len(answer) == 0 or answer[0].lower() == "q":
            break
        if Product.does_barcode_exist(answer):
            p = Product.get_product_by_barcode(answer)
            summary.append(p)
            print(f"Added {p.name} to cart, with the price of {p.price}")
        else:
            print(f"Barcode {answer} does not exist")
    print(f"Summary = {len(summary)} items, total price of "
          f"{ sum([item.price for item in summary])}")
    main()
def main():
    print("Welcome to our Store")
    choice = input("Do you want to (M)anage or (B)uy? ").lower()
    if choice == "m":
        manage()
    elif choice == "b":
        buy()
    else:
        print("Invalid option", file=sys.stderr)
if __name__ == '__main__':
    main()
