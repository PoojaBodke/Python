'''Exercise 3

Add a method to your Rectangle class:
area()
It should return:
length × width
So:
rectangle = Rectangle(10, 5)
print(rectangle.area())
'''
class Rectangle:
    def __init__(self, length,width):
            self.length=length
            self.width=width
    def result(self):
        print(f"Length : {self.length}\nWidth : {self.width}")
    def area(self):
        area=self.length*self.width
        return area
rectangle=Rectangle(10,5)
rectangle.result()
print(rectangle.area())