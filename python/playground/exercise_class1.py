#!/usr/bin/python3

class Cat:
    def __init__(self, name, sound, age):
        self.name1 = name
        self.sound = sound
        self.age = age
    
    def get_name(self):
        return self.name1
    
    def set_age(self, age):
        self.age = age
    
    def get_age(self):
        return self.age

cat1 = Cat("Pussy", "Meow", 30)
print(cat1.age)
cat2 = Cat("Usss", "Meow", 30)
cat1.set_age(100)
print(cat1.get_age())
print(cat1.get_name())
print(cat2.name1)
