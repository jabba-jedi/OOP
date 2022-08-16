#!/usr/bin/env python3

class Person:

    def __init__(self, name:str, surname: str, age: int):
        self.__name = name  # Private Attribute
        self.__surname = surname
        if 1 <= age <= 100:
            self.__age = age
        else:
            raise AttributeError('The age range must be between 1 and 100')
        self.full_name = self.__name + " " + self.__surname

    #getter method
    @property
    def age(self):
        return self.__age

    #setter method
    @age.setter
    def age(self, value):
        if value - self.__age > 1:
            raise AttributeError('You can only get older one year at a time')
            return

        self.__age = value

person1 = Person(name = "Robert", surname = "Johnson", age=27)

print(person1.full_name)
# hehe - works
print(person1._Person__name)

#works
person1.age += 1
print(person1.age)

#fails
person1.age += 10