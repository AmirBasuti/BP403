# Some important commands with strings

# Get ASCII code of a character

print(ord("a"))

# Get character of an ASCII code
print(chr(97))

# len(): returns length of string
string1 = "Hello world"
print(len(string1))

# max(): returns char with the highest ASCII code
print(max(string1))

# min(): returns char with the lowest ASCII code
print(min(string1))

# "in" and "not in" operations
string1 = "Welcome"
string2 = "come"
string3 = "Well"
string4 = "Come"
print(string2 in string1)
print(string3 in string1)
print(string3 not in string1)
print(string4 in string1)

# Euality of strings: ==, !=
string1 = "Hello"
string2 = "hello"
print(string1 == string2)
print(string1 != string2)
print(5 == 3) # same for numbers

# Greater than or less than, >, <, >=, <=
print(5>3)
string1 = "Hello world"
string2 = "Hello galaxy"
print(string1 > string2) # compare strings
print(len(string1) > len(string2)) # compare length of strings

print("--------------------------------------")

# Conditional statements
color = "red"
print("Your slected color is red") # always prints, not desired

print("---------------------------")

# check if the selected color is red
if color == "red":
    print("Your slected color is red")

print("-----------------------------------")
# multiple statements in "if" body

if color == "red":
    print("Your slected color is red")
    print("print was successful")

# note: group indent: ctrl+], ctrl+[

# how write a conditional statement without body:
if color == "red":
    pass

print("-----------------------------------")
# check other existing conditions, we use elif
color = "blue"
if color == "red":
    print("Your slected color is red")
elif color == "blue":
    print("Your slected color is blue")
elif color == "green":
    print("Your slected color is green")

# check other conditions
color = "yello"
if color == "red":
    print("Your slected color is red")
elif color == "blue":
    print("Your slected color is blue")
elif color == "green":
    print("Your slected color is green")
    print("**")
else:
    print("Your selected color is another color")
    print("**")

print("------------------------------")
# importance of indent
# color = input("Please enter a color: ")
color = "green"
if color == "red":
    print("Your slected color is red")
elif color == "blue":
    print("Your slected color is blue")
elif color == "green":
    print("Your slected color is green")
else:
    print("Your selected color is another color")
print("Select either red, blue, or green")

print("------------------------------")
# "if" and "else" in a single line
color = "green"
print("Selected color is red") if color=="red" else print("Selected color isn't red")




# check equality with == and "is"
print("------------------------------")
print("------------------------------")
color = "red"
if color is "red":
    print("Your slected color is red")

color = "blue"
if color is "red":
    print("Your slected color is red")

print("------------------------------")
print("------------------------------")
# Do "==" and "is" always work the same? No
list1 = [4, 7]
list2 = list1
list3 = list(list1)
print("list1: ", list1)
print("list2: ", list2)
print("list3: ", list3)

print("list1 == list2: ", list1 == list2)
print("list1 == list3: ", list1 == list3)

print("list1 is list2: ", list1 is list2)
print("list1 is list3: ", list1 is list3)

# "==" checks if values are equal
# "is" checks if variables point to the same object

# id() represents the unique ID of a Python object
print("ID of list1: ", id(list1))
print("ID of list2: ", id(list2))
print("ID of list3: ", id(list3))

# check variable type
print("------------------------------")
print("------------------------------")
color = "blue"
if type(color) == str:
    print("Your data type is string")
