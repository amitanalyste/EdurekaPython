#!/usr/bin/python
try:
	fh = open("testfile", "w")
	fh.write("This is my test file for exception handling!!")
except:
	print("Error: can\'t find file or read data")
finally:
	fh.close()