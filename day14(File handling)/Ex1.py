'''
Exercise 1
Create a file called:
practice.txt
Write:
I am learning Python.
I want to become a better programmer.
I am practicing every day.
Use "w".

Exercise 2
Read practice.txt and print its entire contents.
Use:
with open(...)

Exercise 3
Read the file line by line and print each line.
Expected:
I am learning Python.
I want to become a better programmer.
I am practicing every day.

Exercise 4 
Append this line:
I am learning Machine Learning.
Then read the file and print everything.
Your output should contain all four lines.
'''
with open("practice.txt","w") as file:
    file.write("I am learning python")
    file.write("\nI want to become a better programmer.")
    file.write("\nI am practicing every day")
with open("practice.txt","a") as file:
    file.write("\nI am learning machine learning")
with open("practice.txt","r") as file:
    content=file.read()
print(content)