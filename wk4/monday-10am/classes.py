import os.path


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    @property
    def name(self):
        return self.__name
    @property
    def price(self):
        return self.__price
    @name.setter
    def name(self, name):
        self.__name = name if len(name) > 2 else "bread"
    @price.setter
    def price(self, price):
        self.__price = price if price >= 1 else 1

    def __str__(self):
        return f"Name={self.name},Price={self.__price}"

    @classmethod
    def expensive_product(cls, name, price=100):
        price = price if price >= 100 else 100
        return cls(name=name, price=price)
    @staticmethod
    def does_barcode_exist(barcode):
        # search barcode in file database, return true or false
        return os.path.exists("data/" + barcode + ".txt")


class Human:
    def __init__(self, name, age):
        self.age = age
        self.name = name
    def __str__(self):
        return f"Name={self.name}, Age={self.age}"
    def attack(self):
        return "Humans do not fight"

class SuperHero(Human):
    def __init__(self, name, age, superhero_name, super_power):
        super().__init__(name, age)
        self.superhero_name = superhero_name
        self.super_power = super_power
    # override: completely change behaviour or previous method

    def __str__(self):
        return super().__str__() + f", SuperHero Name = {self.superhero_name}, " \
                                   f"Super Power = {self.super_power}"

    def attack(self):
        return "My spiddy senses are tingly"

def example2():
    h = Human("Peter Parker", 20)
    sh = SuperHero("Peter Parker 2", 22, "Spiderman", "Creating Webs")
    print(h)
    print(h.attack())
    print(sh)
    print(sh.attack())

def example1():
    p = Product("water", 3)
    print(p)
    p1 = Product.expensive_product("rolex", 500)
    print(p1)

def main():
    example2()

if __name__ == '__main__':
    main()
