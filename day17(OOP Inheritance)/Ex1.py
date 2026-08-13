'''
Exercise 1
Create:
class Animal:
with a method:
speak()
that prints:
Animal makes a sound
Then create:
class Dog(Animal):
Create a Dog object and call:
dog.speak()
'''
class Animal:
    def speak(self):
        print("Animal makes a sound")
class Dog(Animal):
    pass
dog=Dog()
dog.speak()