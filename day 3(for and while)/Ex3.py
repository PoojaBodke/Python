'''
Exercise 3
Ask the user for a number.
Print its multiplication table up to 10.
'''
number=int(input("Enter a number: "))
for i in range(1,11):
    mult=number*i
    print(f"{number}*{i}={mult}")