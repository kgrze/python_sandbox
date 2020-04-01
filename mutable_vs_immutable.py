#!/usr/bin/env python

age = 42
print(id(age))

age = 43
print(id(age)) 
# AHA different ID's int are immutable, every time we set age to other value, another int object is created and age just points to it
print('\n')

class Person:
    def __init__(self, age):
        self.age = age

fab = Person(age=33)
print(fab.age)
print(id(fab))
print(id(fab.age))
fab.age = 34
print(fab.age)
print(id(fab))
print(id(fab.age))