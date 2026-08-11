'''
Exercise 4 — Interview Style
Write:
def find_index(numbers, target):
It should return the index where target appears.
Example:
numbers = [10, 20, 30, 40]
print(find_index(numbers, 30))
'''
'''
def find_index(numbers, target):
    for i,number in enumerate(numbers):
        if number==target:
            return i

numbers = [10, 20, 30, 40]
print(find_index(numbers, 30))

'''
nums = [3,2,2,3]
val = 3   
for index,num in enumerate(nums):
    if num==val:
        nums.remove(val)
print(nums)
print(len(nums))
