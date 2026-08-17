'''
Problem 4 — Sum of Even Numbers
Now we're going to change counting into accumulating.
Given:
nums = [4, 7, 10, 15, 18, 21, 24]
Find the sum of all even numbers.
Expected:
56
'''
nums = [4, 7, 10, 15, 18, 21, 24]
sum=0
for num in nums:
    if num%2==0:
        sum+=num
print(sum)