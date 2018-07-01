newfile = open("edureka.txt", "r")

#for i in range(1,10):
#   newfile.write("\nHello, welcome to Python!")


newfile.seek(5)
print(newfile.read())
print(newfile.tell())



newfile.close()
