# Loop in Python
# "for" loop

myList = [10, 15, 25, 40, 70]
print(type(myList))
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])

# Example 1: for applied to lists
for num in myList:
    print(num)

# Example 2:
for number in myList:
    squaredNumber = number ** 2
    print(f"{number} ^2 =  {squaredNumber}")

# for applied to strings
# Example 1: 
myString = "Hello World"
for character1 in myString:
    print(character1)

# Example 2:
for character in myString:
    print(character.upper())

# Example 3: split a string into words
myString = "This session is on for loop in Python"
myStringList = myString.split()
for word in myStringList:
    print(word)

# Generate a range of numbers
# range(start, stop, step) # start, stop, step should be integer, doesn't include stop
print("range example for positive step value")
rangeOfNumbers = range(1,13,3) # 1,4,7,10
for number in rangeOfNumbers:
    print(number)

print("range example for negative step value")
rangeOfNumbers = range(1,-9,-3) # 1, -2, -5, -8
for number in rangeOfNumbers:
    print(number)

# convert range to list
print(rangeOfNumbers)
print(list(rangeOfNumbers))