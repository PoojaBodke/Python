'''
Exercise 2 — map()
Given:
numbers = [1, 2, 3, 4, 5]
Use map() to multiply every number by 10.
Expected:
[10, 20, 30, 40, 50]
'''

numbers=[1,2,3,4,5]
multi=map(lambda x :x*10,numbers)
print(multi)