# Example Scenario:

# Imagine you are designing a system for a zoo. You have two classes:
# Animal: A base class that contains general attributes and methods for all animals (e.g., name, age, speak()).
# Mammal: A subclass that inherits from Animal and adds specific attributes and methods for mammals (e.g., has_fur, give_birth()).
# Bird: Another subclass that also inherits from Animal but adds attributes and methods specific to birds (e.g., can_fly, lay_eggs()).
# Bat: A subclass that inherits from both Mammal and Bird, combining characteristics of both (e.g., it has fur and can fly).
# In this example, the Bat class demonstrates multiple inheritance by inheriting from both Mammal and Bird

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    
    def speak(self):
        print(f"Animal can speak \n")

class Mammal(Animal):
    def has_fur(self):
        pass 
    
    def give_birth():
        pass  

class Bird(Animal):
    def __init__(self, can_fly):
        self.can_fly = can_fly
        
    def lay_eggs():
        print("Bird laying eggs")

class Bat(Animal, Bird):
    def __init__(self, speak):
        print(f"{speak} ")
    