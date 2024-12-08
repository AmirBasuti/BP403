# String
string1 = "   He said: 'Hello'  "

# Escape characters (\", \')
string2 = " He said: \" Hello "
print(string2)

# Other escape characters (\\, \n, \t, \b)
string3 = "This is \\the first line \n This is the second\tline"
print(string3)

string4 = "Hello\bWorld"
print(string4)

print("-----------------------------")
# String Concatenation
string1 = "Hello"
string2 = "World"
string3 = string1 +        " " + string2
print(string3)

print("-----------------------------")
# Concatenating string with number
string1 = "My age is: "
#string2 = 16 # This leads to error
string2 = 16
string3 = "16"
string4 = string1 + str(string2) # string1 + string2 causes error
string5 = string1 + string3
print(string4)
print(string5)

print("-----------------------------")
# +=
string1 = "Hello"
string2 = "World"
#string1 = string1 + " " + string2
#print(string1)
string1 += " " + string2 # equivalent to string1 = string1 + " " + string2
print(string1)

number1 = 3
number2 = 7
number1 += number2 # equivalent to number1 = number1 + number2
print(number1)

# Also -= *= /=
number1 = 3
number2 = 7
number1 -= number2 # equivalent to number1 = number1 - number2
print(number1)

number1 = 3
number2 = 7
number1 *= number2
print(number1)

number1 = 3
number2 = 7
number1 /= number2 # number1 = number1/number2
print(number1)

# using -= for strings leads to error for example: 
# string1 = "Hello"
# string2 = "World"
# string1 -= string2
# print(string1)

# String interpolation
carName = "Benz"
carColor = "Black"
carModel = "2010"
maxSpeed = 200
result = "Car name is " + carName + " and car color is " + carColor + " and car model is " + carModel
print(result)

# Better solution for printing
result2 = f"Car name is {carName} and car color is {carColor} and car model is {carModel}"
print(result2)

# No problem with numerical values
result3 = f"Car name is {carName} and car color is {carColor} and car maximum speed is {maxSpeed}"
print(result3)

# Another example for different ways of printing
name = "Arman"
score = 95
print("Total score for " + name + " is " + str(score))
print("Total score for %s is %s" % (name, score))
print("Total score for %(n)s is %(s)s" % {'n': name, 's': score})
print("Total score for {} is {}".format(name, score))
print("Total score for {0} is {1}".format(name, score))
print("Total score for {n} is {s}".format(n=name, s=score))
print("Total score for " + str(name) + " is " + str(score))
print("Total score for", name, "is", score)
print(f'Total score for {name} is {score}')


print("---------------------------")
# String indexing
string1 = "Hello"
# index 0 : H, index 1: e, ....
print(string1[1]) # print character at index 1
print(string1[1:4]) # print from index 1 to index 3
print(string1[:]) # print all indices
print(string1[:3]) # print from start to index 2
print(string1[3:]) # print from index 3 to end
# print(string1[5]) # index out of range
string2 = string1[:2]+string1[3:] # form a new string from an existing one
print(string2)
print(string1[-1]) # string1[lengthOfString -1] = string1[5-1] = string1[4], last character
print(string1[-2]) # string1[lengthOfString -2] = string1[5-2] = string1[3], second last character
# print(string1[-6]) # index out of range
print(string1[-4:-1]) # ell
print(string1[4:1]) # prints nothing
print(string1[4:1:-1]) # string1[start:end:step] = "oll" OlL
print(string1[::-1]) # print "Hello" in reverse order: "olleH"
print(string1[-1::-1]) # print "Hello" in reverse order: "olleH"

print("--------------------------")
# Type conversion
carWeight = 2000
print(type(carWeight))
print(carWeight)

# conversion from int to float
carWeightFloat = float(carWeight)
print(type(carWeightFloat))
print(carWeightFloat)

# conversion from int to string
carWeightString = str(carWeight)
print(type(carWeightString))
print(carWeightString)

# conversion from float into int
carWeight = 2000.86
carWeightInt = int(carWeight)
print(type(carWeightInt))
print(carWeightInt)

# conversion from string to float
string1 = "212.56"
number1 = float(string1)
print(type(number1))
print(number1)

# This leads to error
# string1 = "Hello"
# number1 = float(string1)
# print(type(number1))
# print(number1)

# Input from user
print("How long is the car in cm?")
carLength = input() # the outcome of input is string
print("You said that the length is "+carLength+ " cm")
print(f"You said that the length is {carLength} cm")

# convert from cm to inch
carLength = float(carLength)
carLength /= 2.54
print(f"You said that the length is {carLength} inch")

# output to certain some floating points
print("How long is the car in cm?")
carLength = input() # the outcome of input is string
carLength = float(carLength)
carLength /= 2.54
carLength = round(carLength,2) # round to two floating points
print(f"You said that the length is {carLength} inch")

# rounding example
print(round(15.68345,2))
print(round(15.68545,2))