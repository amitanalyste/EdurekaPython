# define Python user-defined exceptions
class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueSmallError(Error):
   """Raised when the input value is too small"""

class ValueLargeError(Error):
   """Raised when the input value is too large"""
   pass

number = 10

while True:
   try:
       in_num = int(input("Enter a number: "))
       if in_num < number:
           raise ValueSmallError
       elif in_num > number:
           raise ValueLargeError
       break
   except ValueSmallError:
       print("This value is too small, try again!")
       print()
   except ValueLargeError:
       print("This value is too large, try again!")
       print()
print("Congratulations! You guessed it correctly.")
