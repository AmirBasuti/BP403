# Variable naming
car = "BMW" # Case sesitive
Car = "Benz"
print(car)
print(Car)

# Assignement to multiple variables
#x = 10
#y = 20
#z = 50
x, y, z = 10, 20, 50
x,y = y,x # swap x and y
print(x)
print(y)
print(z)


# Naming conventions
my_age = 50 # snake case naming
myAge = 50 # Camel case naming
myAgeEqualsThisValue = 50 # Camel case naming
MyAge = 50 # Upper Camel case naming
PI = 3.14 # Constants naming


# Variable name should not be a reserved word in Python
# for = 5 # Error
# while = 6 # Error

# Python is dynamic type
myAge = 50
print(type(myAge))
myAge = 50.5
print(type(myAge))
myAge = "50" # or myAge = '50'
print(type(myAge))
# C++ and C# are static type

# Other variable types (data types)
###################################
# 1- Numeric type
myVar = 50 # int
myVar = 50.5 # float
myVar = 3+2j # complex

# 2- String
myVar = "Hello, This is a string"

# 3- Boolean
myVar = True
myVar = False
print(type(myVar))

# 4- List
myList = [2,3, 5.6, "Hello", [6,7],3]

# 5- Tuple
myTuple = (2,3.6,"Hi")

# 6- Dictionary
myDict = {"Arman": [18,20,19], "Hossein": 20}

# 7- Set
mySet = set([2, 3.6, "Hello", 3.6])

# 8- None
myVar = None
###############################################


# String
mySentence = "Hi, This is Python Course"
mySentence1 = 'Hi, This is Python Course'
# When use ' or "
mySentence = "This is Andrew's book" # string containing '
mySentence =  ' This is a string with " character ' # string containing "

# Another solution for strings containing ' , "
mySentence = 'This is Andrew\'s book'
mySentence1 = " This is a string with \" character"  # string containing 
print(mySentence1)


# Long strings
mySentence = """This is a long string and 
can not be placed in a signle line"""
print(mySentence)

mySentence = "This is a long string and \n can not be placed in a signle line"
print(mySentence)

mySentence = "BCDABCDABCDABCDABCDABCD \
ABCDABCDABCDABCDABCDABCD \
ABCDABCDABCDABCDABCDABCD"
print(mySentence)

mySentence = """BCDABCDABCDABCDABCDABCD
ABCDABCDABCDABCDABCDABCD"""
print(mySentence)


# Strings may contain numbers
myVar = "20"
print(myVar)


# print
print('Hi', end = '\n') # print with default setting
print('Hello')

print('Hi', end = ' ') # print with custom setting
print('Hello')



