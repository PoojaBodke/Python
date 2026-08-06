'''
Exercise 5 (Interview Thinking)
Create:
def largest(numbers):
Example:
nums = [4, 10, 2, 7, 20]
print(largest(nums))
'''
def largest(numbers):
    largest=numbers[0]
    for number in numbers:
        if number>largest:
            largest=number
    return largest

nums=[4,10,2,7,20]
result=largest(nums)
print(result)
