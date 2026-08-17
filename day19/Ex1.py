'''
Given a list of numbers, find the largest number.
Input:
[5, 8, 2, 17, 10, 1]
Output:
17
'''
nums=[5, 8, 2, 17, 10, 1]
greatest=nums[0]
for num in nums:
    if num>greatest:
        greatest=num
print(greatest)