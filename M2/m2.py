import os

newfile = open("foo.txt", "w+")

for i in range(1,10):
    newfile.write("Hello, Welcome to Python\n")

for i in range(1, 10):
    print(newfile.read())

newfile.seek(0)
print(newfile.tell())
