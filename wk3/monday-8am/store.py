import os.path


class Product:
    def __init__(self, barcode, name, price):
        self.barcode = barcode
        self.name = name
        self.price = price
        self.save()

    def __str__(self):
        return f"Barcode={self.barcode}, Name = {self.name}, " \
               f"Price = {self.price}"

    def save(self):
        if not os.path.exists("data"):
            os.mkdir("data")
        f = open("data/" + self.barcode, "w")
        f.write(f"{self.name}\n{self.price}")
        f.close()


def get_product(barcode):
    if barcode in os.listdir("data"):
        info = open("data/" + barcode)
        data = info.readlines()
        p = Product(barcode=barcode, price=float(data[1].strip()), name=data[0].strip())
        return p


def buy():
    print("What do you want to buy?")
    summary = list()
    while True:
        answer = input("Enter barcode of product. "
                       "Or enter (Q)uit to stop loop").lower()
        if answer[0] == "q":
            break
        product = get_product(answer)
        if product:
            print(f"Adding product {product.name} to cart")
            print(f"Price of product is {product.price}")
            summary.append({"name": product.name, "price": product.price, "barcode": product.barcode})

    print(f"You purchased {len(summary)} items. The total price is {sum([item['price'] for item in summary])}")



def manage():
    print("You will be adding a product")
    try:
        barcode = input("Enter barcode: ")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        if barcode in os.listdir("data"):
            raise TypeError()
        Product(name=name, price=price, barcode=barcode)
    except TypeError:
        print("Barcode already exists")
    except ValueError:
        print("Because of invalid price, the product price is 1 cent")
        price = 0.01

def main():
    print("Welcome to our Store")
    choice = input("Would you like to BUY or MANAGE the store?")\
        .lower().strip()
    if choice in ["buy", "manage"]:
        if choice == "buy":
            buy()
        elif choice == "manage":
            manage()
    else:
        print("Invalid option")


if __name__ == '__main__':
    main()
