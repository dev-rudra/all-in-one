#!/usr/bin/python3

# Define a new class Dog
class Dog:
    """
    constructor method __init__.
    It's automatically called when
    a new object of class is created

    self => referes to the instance of the class.

    name, bread => are the parameters 
    that are passed when creating the dog object.
    """
    def __init__(self, name, bread):
        """ these are the attributes of a class """
        self.name = name
        self.bread = bread
    
    def bark(self):
        print(f"{self.name} says woof!")

    def get_name(self):
        return self.name

dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()

print(dog1.name)
print(dog1.get_name())
