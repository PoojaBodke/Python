'''
Exercise 2
Create:
class Person:
with:
name
age
Then create:
class Student(Person):
Student should additionally have:
degree
Use super().
Then:
student = Student("Pooja", 24, "Computer Science")
'''
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class Student(person):
    def __init__(self,name,age,degree):
        super().__init__(name,age)
        self.degree=degree
    def result(self):
        return self.name,self.age,self.degree

student = Student("Pooja", 24, "Computer Science")
student.result()
print(student.name)
print(student.age)
print(student.degree)
