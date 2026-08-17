'''
Problem 3 — Count Even Numbers
Given:
nums = [4, 7, 10, 15, 18, 21, 24]
Find how many numbers are even.
Expected:
4
'''
nums = [4, 7, 10, 15, 18, 21, 24]
count=0
for num in nums:
    if num%2==0:
        count+=1

print(count)