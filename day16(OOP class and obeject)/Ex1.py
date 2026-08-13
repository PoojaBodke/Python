'''
Exercise 1
Create a class:
Person
It should have:
name
age
Create an object:
Name: Pooja
Age: 24
Then print both.
'''
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def result(self):
        print(f"Name : {self.name} \nAge: {self.age}")
student1=Person("Pooja","24")
student1.result()