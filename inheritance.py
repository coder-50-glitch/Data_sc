class Animal:
    def __init__(self, name, habitat):
        self.name    = name
        self.habitat = habitat

class Dog(Animal):
    def __init__(self, name, habitat, breed):
        super().__init__(name, habitat)   # cleaner — no class name needed
        self.breed = breed

class Parrot(Animal):
    def __init__(self, name, habitat, phrase):
        super().__init__(name, habitat)
        self.phrase = phrase