# Some Definitions: بعضی تعاریف
# script: some lines of code
# Module: is a file that contains some functions.
# Package: is a collection of modules.
# Library: is a collection of packages.
# Framework: is a collection of libraries.


# __name__ in python:
# __name__: is a special variable in Python.

# __name__ is a built-in variable which evaluates to the
#  name of the current module. Thus it can be used to check
#  whether the current script is being run on its own or being imported

print(__name__)

print("---------------------")
# if __name__ == "__main__": 
#     print ("session32 is being run directly")
# else: 
#     print ("session32 is being imported")


from myFirstFile import printName1
from mySecondFile import printName2

def printName():
    print(f"__name__ in session32-name.py is {__name__}")

printName()
printName1()
printName2()