'''
Exercise 4 — Interview Thinking
Given:
words = ["apple", "cat", "banana", "dog", "elephant"]
Use filter() to keep words whose length is greater than 4.
Expected:
["apple", "banana", "elephant"]
'''
words = ["apple", "cat", "banana", "dog", "elephant"]
length=list(filter(lambda x: len(x)>4,words))
print(length)