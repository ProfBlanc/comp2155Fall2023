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
        f = open("data/" + self.barcode + ".txt", "w")
        f.write(f"{self.name}\n{self.price}")
        f.close()


inventory = os.listdir("data")


def get_product(barcode):
    if ".txt" not in barcode:
        barcode += ".txt"
    if barcode in inventory:
        info = open("data/" + barcode)
        return info.readlines()


def buy():
    print("What do you want to buy?")
    while True:
        answer = input("Enter barcode of product. "
                       "Or enter (Q)uit to stop loop").lower()
        if answer[0] == "q":
            break
        product_details = get_product(answer + ".txt")
        if product_details:
            print(f"Adding product {product_details[0].strip()} to cart")
            print(f"Price of product is {product_details[1]}")


def manage():
    print("You will be adding a product")
    # TODO: only add products with unique barcode
    try:
        barcode = input("Enter barcode: ")
        name = input("Enter name: ")
        price = float(input("Enter price: "))
        p = Product(name=name, price=price, barcode=barcode)
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
