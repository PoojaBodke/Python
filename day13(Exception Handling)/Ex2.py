'''
Write a program that asks for two numbers and divides them.
Handle both:
User enters text instead of a number → "Invalid number"
User enters 0 as the second number → "Cannot divide by zero"
You'll need two different exceptions.
'''
try:
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    print(a/b)
except ValueError:
    print("Enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")