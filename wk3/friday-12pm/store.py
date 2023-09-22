"""
Create a store module that will allow a store owner
to MANAGE the store and a consumer to BUY

"""
import os.path
import sys
class Product:
    base_dir = "data"

    def __init__(self, barcode, name, price):
        self.name = name
        self.price = price
        self.barcode = barcode
        self.check_dir()
        self.write()

    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @property
    def barcode(self):
        return self.__barcode
    @name.setter
    def name(self, name):
        self.__name = name
    @price.setter
    def price(self, price):
        self.__price = price
    @barcode.setter
    def barcode(self, barcode):
        self.__barcode = barcode

    def check_dir(self):
        if not os.path.exists(self.base_dir):
            os.mkdir(self.base_dir)

    def write(self):
        f = open(self.base_dir + "/" + self.barcode + ".txt", "w")
        f.write(f"{self.name}\n{self.price}")
        f.close()
    @staticmethod
    def does_exist(barcode):
        return os.path.exists(Product.base_dir + "/" + barcode + ".txt")

    @classmethod
    def get_product_by_barcode(cls, barcode):
        f = open(Product.base_dir + "/" + barcode + ".txt", "r")
        contents = f.readlines()

        return cls(barcode=barcode, name=contents[0].strip(),
                   price=float(contents[1].strip()))

def manage():
    """
    Ask the store owner for: barcode, name, price
    ADD this product to a directory: many .txt files
            barcode.txt, where barcode = numbers
    """
    while True:
        try:
            barcode = input("Enter barcode: ")
            name = input("Enter name: ")
            price = float(input("Enter price: "))
            p = Product(name=name, price=price,
                        barcode=barcode)
            answer = input("Do you want to add another product? y/n: ")
            if answer[0].lower() != "y":
                break
        except ValueError:
            print("Invalid Price", file=sys.stderr)

    main()
def buy():
    summary = list()
    print("Welcome to our shopping center")
    while True:
        answer = input("Enter barcode or (Q)uit to stop shopping")
        if answer[0].lower() == "q":
            break
        if not Product.does_exist(answer):
            print(f"Barcode {answer} does not exist")
        else:
            p = Product.get_product_by_barcode(answer)
            summary.append(p)
            print(f"You have added {p.name} to cart with price of {p.price}")

    print(f"Summary of items = Total Items {len(summary)}, Total Price "
          f"= { sum( [ item.price for item in summary ] )  }")

    main()
def main():
    print("Welcome to our store")
    choice = input("Do you want to MANAGE or BUY?: ")
    if choice[0].lower() == "m":
        manage()
    elif choice[0].lower() == "b":
        buy()
    else:
        print("Invalid option", file=sys.stderr)
if __name__ == '__main__':
    main()
