"""
Classes (usually noun)
have two things
    attributes (adjectives)
    methods (verbs)
    
ex Class animal
    attributes: name, hunger, diet
    methods: move(), eat()
    
Object-orientated design
    - model objects with classes 
        - attributes 
        - methods
    - considered programming paradigm 
    - allows us to establish relationships between objects
    
Class constructor:
    - special type of method that gives object's attribtes their initial values
    - __init() in Python
    
self keyword --> indicates class-level variable 
"""

# animal class example - start with capital letter


class Animal:
    def __init(self, name, hunger, diet):
        self.name = name
        self.hunger = hunger
        self.diet = diet

    def eat(self, food):
        if food > 0 and hunger < 25:
            hunger += food
