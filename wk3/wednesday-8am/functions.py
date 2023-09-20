class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__height = 20
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name if len(name) > 2 else "Ben"
    def getHeight(self):
        return self.__height
    def setHeight(self, height):
        self.__height = height if height >= 20 else 20

    # getters and setters
    @property  # decorator
    def age(self):
        return "I am " + str(self.__age) + " years old"

    @age.setter  # change a value
    def age(self, age):
        if 0 <= age <= 150:
            self.__age = age
        else:
            self.__age = 2

    def __str__(self):
        return f"Name = {self.name}, Age={self.age}"

    def isAdult(self):
        return self.__age >= 18

    @staticmethod  # method that belongs to class. no relation to class
    def hasOddChars(value):
        return len(value) % 2 == 1

    @classmethod  # factory => create a category of class
    def highschooler(cls, name, age):
        age = age if age >=14 and age <= 19 else 14
        name = name if len(name) > 2 else "Highschooler"
        return cls(name, age)

    @classmethod
    def elder(cls, name="Old Person", age=110):
        return cls(name, age)

    # define functionality of operators

    def __add__(self, other):
        if isinstance(other, Person):
            return Person(name = f"{self.__name}-{other.__name}", age= (self.__age + other.__age) / 2 )
        else:
            return Person(name=self.__name + "-unknown", age= self.__age)
    def __mul__(self, other):
        return f"{self.__name} x other"



greeting = "hello"


def add(n1, n2):
    return n1 + n2

