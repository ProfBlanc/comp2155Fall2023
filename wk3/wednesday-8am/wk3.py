# import functions
#
# r1 = functions.Person("Ben", 100)
#
# r2 = functions.add(1, 2)
#
# print(functions.greeting)

# from functions import *
#
# p = Person("Ben", 100)
#
# r1 = add(1,2)
# print(greeting)

from functions import greeting, Person

print(greeting)
# add()
# p = Person("Ben",100)
# print(p)
# print(p.age)
# p.age = 90
# print(p.age)

p = Person("B", -100)
print(p)

p.getHeight()
p.setHeight(40)

print(p.isAdult())
print(Person.hasOddChars("hello"))


billy = Person.highschooler("Billy", 15)
print(billy)
elder = Person.elder()


combined = p + billy
print(combined)

m = elder * 10
print(m)

m1 = elder + "hello"
print(m1)
