#!/usr/bin/python3
# oop3.py by Bill Weinman <http://bw.org/contact/>
# OOP/Polymorphism example in Python
# This is an exercise file from Python 3 Essential Training on lynda.com
# Copyright (c) 2010 The BearHeart Group, LLC

# -- VIEW --

class AnimalActions:
    def bark(self): return self._doAction('bark')            # _doAction
    def fur(self): return self._doAction('fur')              # _doAction
    def quack(self): return self._doAction('quack')          # _doAction
    def feathers(self): return self._doAction('feathers')    # _doAction

    def _doAction(self, action):                             # _doAction
        if action in self.strings:
            return self.strings[action]
        else:
            return 'The {} has no {}'.format(self.animalName(), action) #  The has no

    def animalName(self):
        return self.__class__.__name__.lower()

# -- MODEL -- 

class Duck(AnimalActions):
    strings = dict(
        quack = "Quaaaaak!",
        feathers = "The duck has gray and white feathers."
    )
 
class Person(AnimalActions):
    strings = dict(
        bark = "The person says woof!",
        fur = "The person puts on a fur coat.",
        quack = "The person imitates a duck.",
        feathers = "The person takes a feather from the ground and shows it."
    )

class Dog(AnimalActions):
    strings = dict(
        bark = "Arf!",
        fur = "The dog has white fur with black spots.",
    )

# -- CONTROLLER -- 

def in_the_doghouse(dog):
    print(dog.bark())
    print(dog.fur())

def in_the_forest(duck):
    print(duck.quack())
    print(duck.feathers())
 
def main():
    donald = Duck()
    john = Person()
    fido = Dog()

    print("-- In the forest:")
    for o in ( donald, john, fido ):  # The dog has no ...
        in_the_forest(o)

    print("-- In the doghouse:")         
    for o in ( donald, john, fido ):  # The duck has no ...
        in_the_doghouse(o)
 
if __name__ == "__main__": main()
