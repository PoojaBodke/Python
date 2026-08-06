'''
Find the largest number in this list without using max().
numbers = [5, 8, 2, 17, 10, 1]
'''
numbers = [5, 8, 2, 17, 10, 1]
numbers.sort()
print(numbers[-1])

'''
Exercise 4

Find the smallest number without using min().
'''
numbers = [5, 8, 2, 17, 10, 1]
numbers.sort()
print(numbers[0])

'''
Exercise 5 ⭐ (Interview Style)
Count how many even numbers are in:
numbers = [4, 7, 10, 15, 18, 21, 24]
'''
numbers = [4, 7, 10, 15, 18, 21, 24]
sum=0
for number in numbers:
    if number%2==0:
        sum=sum+1
print(sum)