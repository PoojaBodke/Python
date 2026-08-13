'''
Exercise 4
Create:
class Calculator:
with methods:
add()
subtract()
multiply()
divide()
Example:
calc = Calculator()
print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))
'''
class Calculator:

    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
        print(f"Substraction: {substract}")
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("Cannot divide by zero")
calc = Calculator()

print(calc.add(10, 5))
print(calc.subtract(10, 5))
print(calc.multiply(10, 5))
print(calc.divide(10, 5))