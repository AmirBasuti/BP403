# Underscore (underline) and double underscore

# underscore applications

# 1- ignoring values
# Example
# a,b = (1,2,3) # error
a, _, b = (1, 2, 3)
print(a, b)


# Example
def myFunc(x, y):
    return x+y, x-y, x*y, x/y

# mySum, myDiff, myProd, myDiv = myFunc(5,4)
mySum, _, _, myDiv = myFunc(5, 4)
print(mySum, myDiv)

print("-----------------------")
# ignoring multiple values
# *(variable) used to assign multiple value to a variable as list while unpacking
# it's called "Extended Unpacking"
a, *_, b = (7, 6, 5, 4, 3, 2, 1)
c, d, *_ = (7, 6, 5, 4, 3, 2, 1)
print(a, b)
print(c,d)

print("-------------------------------------")
# 2- Use "_" in loops
for num in range(10):
    print("Hi")
    print(num)

for _ in range(10):
    print("Hi")

# 3- separating digits
x = 100000000
print(x)
x = 100_000_000
print(x)
y = 1_00_00_00_00
print(y)
z = 0b10_010_100 # base 2
print(z)
w = 0x180_0_10_9_00 # base 16
print(w)



print("----------------------------------")
############################################
# single pre-underscore: _name
# It is used for internal and private use. But does not do anything special
# Example:
class car:
    def __init__(self):
        self.name = "Benz"
        self._model = 2003

benz = car()
print(benz.name)
print(benz._model)
# change attributes
benz.name = "another name"
benz._model = 2010
print(benz.name)
print(benz._model)

# Example
# import functions: function with starting underscore could not be accessed
from myModule import *
print(myfunc1(1))
# print(_myfunc2(4)) # error

# Solution
import myModule as mm
print(mm.myfunc1(5))
print(mm._myfunc2(8))

# Another solution
from myModule import _myfunc2
print(_myfunc2(8))

print("--------------------")
# single post-underscore: name_
# when we want to use a Python keyword as the name of variable
# for = 2 # Error
for_ = 2 # No error

# Example:
# def myFunc(class): Error
#     return 2*class

def myFunc(class_): #No Error
    return 2*class_

# double pre-underscore: __name
# used for renaming variables to avoid name conflicts (name mangling)

# Example
class myClass:
    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3

myObject = myClass()
print(dir(myObject)) # we see "a", "_b" but not "__c" (we see "_myClass__c")
print(myObject.a)
print(myObject._b)
# print(myObject.__c) # error
print(myObject._myClass__c)

# Double post-underscore has not any special meaning
x = 3
x__ = 5

# Double Pre And Post Underscores
# In Python, you will find different names which start and end with the double underscore. 
# They are called as magic methods.
# Examples: __init__, __str__,
# It's better to stay away from them, to avoid clashes.