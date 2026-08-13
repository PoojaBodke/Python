'''
Exercise 2
Create:
class Rectangle:
It should have:
length
width
Create:
rectangle = Rectangle(10, 5)
Then print:
Length: 10
Width: 5
'''
class Rectangle:
    def __init__(self, length,width):
        self.length=length
        self.width=width
    def result(self):
        print(f"Length : {self.length}\nWidth : {self.width}")
rectangle=Rectangle(10,5)
rectangle.result()