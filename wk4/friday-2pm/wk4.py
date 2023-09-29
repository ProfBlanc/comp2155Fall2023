"""
Using a previous existing class to create
a new class
"""
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
        self.__name = name if len(name) > 2 else "Product"
    @price.setter
    def price(self, price):
        self.__price = price if isinstance(price, int) \
        or isinstance(price, float) and price >= 1 else 1
    def __str__(self):
        return f"Name={self.name}, Price={self.__price}"
    def __add__(self, other):
        if isinstance(other, Product):
            return Product(name=self.__name + "-" + other.__name,
                           price=round(
                               (self.__price + other.__price) / 2, 2)
                           )

# super        sub
# previous          newer version

# parent            child
# base              derived
class HeavyProduct(Product):
    def __init__(self, name, price, weight=50):
        super().__init__(name, price)
        self.weight = weight
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight):
        self.__weight = weight if isinstance(weight, int) \
                                  and weight >= 50 else 50
    def __str__(self):
        return super().__str__() + f", Weight={self.__weight}"

p1 = Product("rice", 3)
p2 = Product("beans", 4)
p3 = p1 + p2
print(p1, p2, p3, sep='\n')

hp1 = HeavyProduct("desk", 399.99)
print(hp1)

print(isinstance(hp1, Product))

print(isinstance(p1, HeavyProduct))

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name={self.name}, Age={self.age}"
class SuperHero(Human):
    def __init__(self, name,age,super_hero_name, super_power):
        super().__init__(name, age)
        self.super_hero_name = super_hero_name
        self.super_power = super_power

    # pass a human and only ask for superhero name and power
    @classmethod
    def from_human(cls, human, superhero_name, super_power):
        if not isinstance(human, Human):
            return None
        return cls(human.name, human.age, superhero_name, super_power)

    def __str__(self):
        return super().__str__() + f", " \
                                   f"SuperHeroName={self.super_hero_name}, " \
                                   f"SuperPower={self.super_power}"

h = Human("Peter Parker", 20)
sh = SuperHero("Peter Parker", 20, "Spiderman", "Creating webs")
print(h, sh, sep='\n')

sm = SuperHero.from_human(h, "Spiderman", "Creating Webs")
print(sm)

class Lion:
    somevalue = "hello"
    def __init__(self, name, scariness):
        self.name = name
        self.scariness = scariness
    def __str__(self):
        return f"Lion-Name={self.name}, Scariness={self.scariness}"

class Tiger:
    def __init__(self, teeth):
        self.teeth = teeth
        self.stripes = "stripes"
    def __str__(self):
        return f"Name={self.teeth}, Scariness={self.stripes}"

class Liger(Lion, Tiger):
    pass

l = Liger("a","b")

print(l)

