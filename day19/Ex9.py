'''
Problem 9 — First Unique Character
Now we're going to combine dictionary + loop, which you've already practiced.
Given:
s = "leetcode"
Find the first character that appears only once.
Expected:
"l"
Another example:
s = "aabbcddee"
Expected:
"c"
'''
s = "leetcode"
t=""
count={}
for ch in s:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
print(count)
for key, value in count.items():
    if value==1:
        print(key,value)
        break
        
    
