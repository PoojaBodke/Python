'''
Exercise 5 — Interview/Data Thinking

Create a file containing:

Python
Java
Python
C++
Python
Java

Read the file and count how many times each programming language appears.
'''
with open("practice.txt","w") as file:
    file.write("Python")
    file.write("\nJava")
    file.write("\nCPP")
    file.write("\nJava")
    file.write("\nPython")
count={}
with open("practice.txt", "r") as file:
    for line in file:
        line = line.strip()
        if line in count:
            count[line]+=1
        else:
            count[line]=1
print(count)