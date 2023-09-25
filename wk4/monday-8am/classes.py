import os
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
        self.__name = name if len(name) > 2 else "Rice"
    @price.setter
    def price(self, price):
        self.__price = price if isinstance(price, float) and price >= 1 else 0

    def __str__(self):
        return f"Name={self.name}, Price={self.price}"

    @classmethod
    def create_long_product_name(cls, name):
        name = name if len(name) >5 else "abcdef"
        return cls(name=name, price=1234)


class HeavyProduct(Product):
    def __init__(self, name, price, weight):
        super().__init__(name, price)
        self.weight = weight
    def __str__(self):
        return super().__str__() + f", Weight={self.weight}"
    def can_be_lifted(self, weight_of_human):
        return weight_of_human * 2 >= self.weight

def example1():
    p = Product(name="beans", price=-5)
    print(p)

    p1 = Product.create_long_product_name("helloworld")
    print(p1)


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name={self.name}, Age={self.age}"
    def attack(self):
        return "Cannot fight"
# super class (older class), sub class (newer class)
class SuperHero(Human):
    def __init__(self, human_name, age, superhero_name):
        super().__init__(name=human_name, age=age)
        self.superhero_name = superhero_name
    def __str__(self):
        return super().__str__() + ", SuperHero Name = " + self.superhero_name
    def attack(self):
        return "Call Alfred and get Batmobile"
def example2():
    h = Human("Bruce Wayne", 100)
    print(h)
    sh = SuperHero("Bruce Wayne", 100, "Batman")
    print(sh.attack())
    print(sh)

def example3():
    p = Product("Water", 2)
    hp = HeavyProduct("Dresser", 1000.0, weight=300)
    print(hp)
def main():
    example3()

if __name__ == '__main__':
    main()
