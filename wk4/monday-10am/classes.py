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


class HeavyProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        if weight < 50:
            raise ValueError("Heavy products must be at least 50 pounds")
        self.__weight = weight
    def __str__(self):
        return super().__str__() + f",Weight={self.weight}"
    def can_be_lifted(self, human_weight):
        return human_weight >= self.weight * 2

class Lion:
    def __init__(self, name, paws):
        self.name = name
        self.paws = paws
    def __str__(self):
        return f"Name={self.name}, Paws={self.paws}"
    def roar(self):
        return "Roar Lion!"
    def some_lion_method(self):
        return "Prof lost his creative juices"

class Tiger:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def __str__(self):
        return f"Name={self.name}, Weight={self.weight}"
    def roar(self):
        return "Tiger also roars"
    def some_tiger_method(self):
        return "Another random method example"

class Liger(Lion, Tiger):
    def __init__(self, f1, f2):
        super.__init__(f1, f2)


def example4():
    liger = Liger("Liger", 10)
    print(liger.roar())
    print(liger.name, liger.paws, liger.weight)
def example3():
    p = Product("juice", 5)
    hp = HeavyProduct("Dresser", 1000, 200)
    print(p)
    print(hp)
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
    example4()

if __name__ == '__main__':
    main()
