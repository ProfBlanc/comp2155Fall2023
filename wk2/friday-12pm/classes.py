class Product:
    def __init__(self, name, description, price):
        self.__name = name
        self.__description = description
        self.__price = price

    def __str__(self):
        return f"Name = {self.__name}, " \
               f"Description = {self.__description}," \
               f"Price = {self.__price}"

    # getters and setters
    @property
    def name(self):  # getter
        return self.__name

    @name.setter
    def name(self, new_value):
        if len(new_value) < 3:
            raise ValueError("Name must be at least 3 chars")
        self.__name = new_value

    def is_expensive(self):
        return self.__price > 100

shoes = Product(name="Shoes", description="Cool Shoes",
                price=5.5)
print(shoes)
shoes.name = "bl"
print(shoes)
print(shoes.is_expensive())
