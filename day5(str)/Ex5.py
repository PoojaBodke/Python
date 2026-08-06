
'''
Exercise 5 ⭐⭐
Reverse a string without using:
[::-1]
reversed()
'''

word="apple"
wo=""
length=len(word)
for i in range(1, length+1):
    wo+=word[-i]
print(wo)


