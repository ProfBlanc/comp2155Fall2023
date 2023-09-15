class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Name={self.name}, Description={self.description}, " \
               f"Price={self.price}"

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_value):
        if len(new_value) < 3:
            raise ValueError("Name must be at least 3 chars")
        self.__name = new_value

    def is_expensive(self):
        return self.price > 100

rice = Product(name="rice", description="plain rice", price=5.75)
print(rice)
# rice.name = "ab"  # throws error
rice.name = "abc"
print(rice)
print(rice.is_expensive())
