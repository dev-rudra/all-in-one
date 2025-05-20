#!/usr/bin/python3

"""
Inheritance in python

Inheritance is a core concept in OOP that allows a class(child or subclass) to 
inherit the properties and methods of another class(parent or supperclass)

It helps on:

1. Reuse code (don't repeat yourself)
2. Organize code logically
3. Extend or override behavior
"""

# Example of repeat code

class Horse:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Woof!")

class Cow:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print("Meow")

# In the above two classes everything is same except the sound string

#################################
#           INHERITANCE         #
#################################

# parent or supperclass
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"My name is {self.name} and I'm {self.age} years old!")

# Child/derived class inherits from Animal (supper class)
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

class Dog(Animal):
    """
    How to add new attributes only for this class
    """
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print(f"{self.name} says Woof!")
    
    def show(self):
        print(f"My name is {self.name} and I'm {self.age} years old and I'm {self.color}.")

# create a new instance of a class
animal = Animal("dog", 20)
animal.show()

print("\n")
print("I'm a Cat class")
cat = Cat("luna", 2)
cat.speak()
cat.show()

print("\n")
print("I'm Dog class")
dog = Dog("Charllie", 10, "Brown")
dog.speak()
dog.show()
