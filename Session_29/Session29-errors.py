# Error handling in Python
#  Errors that occur at runtime (after passing the syntax test)
#     are called exceptions or logical errors.

# Some important error types
# SyntaxError
# Examples
# for = 1
# None = 2
# return 3
# def helloWorld
# def helloWorld()

# x = 2;; # ";" is not used in Python (used in C++), but it is used to put 
#            more than one command in a sigle line
# For Example for assigning x=2 and put y=3, we can:
# Method 1:
x, y = 2,3
# Method 2:
x = 2
y = 3
# Method 3:
x=2; y=3


# indentation error
#  def helloWorld():

# NameError
# print(z)

# TypeError
print(len("Hello")) # OK
#print(len(20)) #TypeError
print("Hello" + " Bye") # this is ok
# print("Hello" + 12) # TypeError

# IndexError
numList = [10, 20, 30]
# print(numList[6])

# ValueError
myString = "Hello"
# myNum = int(myString)

# KeyError
myDict = {"A": 1, "B": 10}
# print(myDict["C"])

# AttributeError
myString = "Hello"
# myString.x

# list of Python errors: programiz.com/python-programming/exceptions

print("--------------------------")
# raise error
# Example:
# raise IndexError("In this code there is an index error!!!")

# Example: We want the input to be of string type
def myColor(inputColor):
    if type(inputColor) is not str:
        raise TypeError("Color name must be a string")
    else:
        print(f"Your selected color: {inputColor}")
myColor(12)

