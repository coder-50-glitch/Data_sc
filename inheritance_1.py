class Animal:                     # parent class
    def display(self):
        print("I am an animal.")

class Dog(Animal):                # child class — inherits from Animal
    pass

d = Dog()
d.display()   

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

    @abstractmethod          # every child MUST implement this
    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)
        self.breed = breed

    def speak(self):         # required — concrete implementation
       print(f"{self.name} ({self.breed}) says: Woof! Woof!")

d = Dog("Bruno", "Home", "Labrador")
d.speak()   # Output: Bruno (Labrador) says: Woof! Woof!