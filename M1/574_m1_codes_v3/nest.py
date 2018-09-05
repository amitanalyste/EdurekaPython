count=1
for i in range(10):
    print(str(i)*i)

    for j in range(0,i):
        count=count+1

#nested loops
for i in range(1,3):
    for j in range(1,2):
        print("*")