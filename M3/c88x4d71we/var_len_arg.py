def info(user,*users):
    print("Users of Python:")
    print(user)
    for var in users:
        print("Users of Python")
        print(var)
        return()

info("Annie")
info("Annie","Dave")

#Another Example

def myFunction(arg1, arg2, arg3, *args, **kwargs):
    print('First Normal Argument : ' + str(arg1))
    print('Second Normal Argument : ' + str(arg2))
    print('Third Normal Argument : ' + str(arg3))
    print('Non-keyworded Argument : ' + str(args))
    print('Keyworded Argument : ' + str(kwargs))

myFunction(1, 2, 3, 4, 5, 6, 7, name='Mandar', country='India', age=25)