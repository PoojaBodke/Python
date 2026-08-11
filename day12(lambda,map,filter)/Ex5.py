'''
Exercise 5 — Combine map() + filter()
Given:
numbers = [1, 2, 3, 4, 5, 6]
First keep only the even numbers, then multiply them by 10.
Expected:
[20, 40, 60]
'''
numbers = [1, 2, 3, 4, 5, 6]
num=list(filter(lambda x: x%2==0,numbers))
num2=list(map(lambda x: x*10,num))
print(num2)