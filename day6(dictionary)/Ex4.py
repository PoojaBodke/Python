'''Exercise 5 (Interview Thinking)
Count the frequency of characters.
Example:
Input:
apple
Expected Output:
{
    'a': 1,
    'p': 2,
    'l': 1,
    'e': 1
}
'''

word="apple"
count={}
for ch in word:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)




