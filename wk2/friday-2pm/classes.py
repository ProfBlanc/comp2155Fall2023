class Product:
    def __init__(self, name, description, price):
        self.__name = name
        self.__price = price
        self.__description = description
    
    def __str__(self):
        return f"Name={self.__name}, Description={self.__description}, Price = {self.__price}"
    
    def is_expensive(self):
        return self.__price > 100
    
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_value):
        if len(new_value) < 3:
            raise ValueError("Name should be at least 3 characters")
        self.__name = new_value
shoe = Product("Shoes", "cool shoes", 225.50)
print(shoe)
shoe.name = "Cool Shoes"
print(shoe)
print(shoe.is_expensive())
