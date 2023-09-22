"""
This module will be a store where
    1) Store Owners can add product
        MANAGE product
            entering barcode, name, price
                add a file
                    barcode.txt
                        product name
                        product price
    2) Consumers can purchase
        enter a barcode
        searches system to get product details
        Found: add product to the cart
        Not found: sorry message

"""
import os.path
import sys


class Product:
    base_dir = "data"
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.save_product()
    def save_product(self):
        self.check_directory()
        f = open(self.base_dir + "/" + self.barcode + ".txt", "w")
        f.write(f"{self.name}\n{self.price}")

    def check_directory(self):
        if not os.path.exists(Product.base_dir):
            os.mkdir(Product.base_dir)

    @property
    def barcode(self):
        return self.__barcode
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price

    @barcode.setter
    def barcode(self, barcode):
        if not barcode.isdigit():
            raise ValueError("Barcode is invalid")
        self.__barcode = barcode

    @name.setter
    def name(self, name):
        self.__name = name
    @price.setter
    def price(self, price):
        try:
            self.__price = float(price)
        except:
            raise ValueError("Price is not a float")

def manage():
    print("You will be entering products")
    while True:
        try:
            barcode = input("Enter barcode: ")
            name = input("Enter name: ")
            price = input("Enter price: ")
            p = Product(name=name, barcode=barcode, price=price)
        except ValueError as e:
            print(e, file=sys.stderr)
def buy():
    pass
def main():
    print("Welcome to our store")
    choice = input("Do you want to (M)anage or (B)uy? ").lower()
    if choice[0] == "m":
        manage()
    elif choice[0] == "b":
        buy()
    else:
        print("Invalid option", file=sys.stderr)
if __name__ == '__main__':
    main()
