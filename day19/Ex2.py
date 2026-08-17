'''
Problem 2
Now let's change it slightly.
Given:
nums = [5, 8, 2, 17, 10, 1]
Find the smallest number.
'''
nums = [5, 8, 2, 17, 10, 1]
smallest=nums[0]
for num in nums:
    if num<smallest:
        smallest=num
print(smallest)