"""
Inheritance in Python

Base class other class use while adding extra qualities to it

Allows us to define hierarchical relationships

Avoid typing redundant code 

Python supports multiple inheritance
    - child classes/sub classes can inherit code from multiple parent classes 
"""

# Base class


class Animal:
    def __init__(self, name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and hunger < 25:
            hunger += food


# Dog inherits from animal class

class Dog(Animal):
    def __init__(self, name, hunger, diet, breed, indoor):
        super().__init__(name, hunger, diet)  # calls parent constructor
        self.breed = breed
        self.indoor = indoor

    def fetch(self, ballX, ballY):
        print('%s fetched the ball' % (self.name))

    def eat(self, food):
        if food > 0 and self.hunger < 90:
            self.hunger += food


fido = Dog('Fido', 80, 'Meat', 'Lab', True)
print(fido.hunger)
fido.eat(10)
print(fido.hunger)
fido.fetch(2, 4)
