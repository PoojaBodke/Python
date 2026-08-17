'''
Problem 7 — Reverse a List
Now let's move to a different pattern.
Given:
nums = [1, 2, 3, 4, 5]
Expected:
[5, 4, 3, 2, 1]
'''
nums= [10, 2, 3, 4, 5]
reverse=[]
for i in range(1,6):
    reverse.append(nums[-i])
print(reverse)