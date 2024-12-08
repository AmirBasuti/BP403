# len: returns length of an object
# Example:
myString = "Hello"
print(len(myString))
# Example
myList = [2, 5, 7]
print(len(myList))

print("-------------------------")
# abs: returns absolute value of a number
print(abs(-6))

# Example: abs of a list
#print(abs([2,3,-7,0,-4,3])) # Error
numList = [2,3,-7,0,-4,3]
absList = [abs(item) for item in numList]
print(numList)
print(absList)

# abs of complex numbers: returns absolute value
# j: square root of -1
complexNum = 3 + 4j
print(abs(complexNum))

# sum: returns sum of items of an iterable
numbers = [2.5, 3, 4, -5]
numbersSum = sum(numbers) # 2.5+3+4+(-5)
print(numbersSum)
numbersSum = sum(numbers, 10) # 2.5+3+4+(-5)+10
print(numbersSum)

# round: rounds a number to some floating points
roundedNum = round(2.76543, 2)
print(roundedNum)

# print an integer to two decimal places
intNumber = 2
print(f"The number with two decimal digits is: {intNumber:.2f}")

# print an integer to two decimal places
floatNumber = 2.76543
print(f"The number with two decimal digits is: {floatNumber:.2f}")

print("------------------")
# zip: takes some iterables and aggregates them
# Example:
fruitName = ["apple", "orange", "banana"]
fruitPrice = [10, 15, 30, 40]
result = zip(fruitName, fruitPrice)
print(result)
resultList = list(result)
print(resultList)

print("-------------------------")
# Example:
fruitName = ["apple", "orange", "banana"]
fruitPrice = (10, 15, 30, 40)
fruitWeight = [2, 2, 1]
result = zip(fruitName, fruitPrice, fruitWeight)
print(result)
resultList = list(result)
print(resultList)

print("--------------")
# unzip
fruitName2, fruitPrice2, fruitWeight2 = zip(*resultList)
print(fruitName2)
print(fruitPrice2)
print(fruitWeight2)

print("-----------------------")
# Note: zip produces an iterator that can be 
# used only once. After that it is empty.
# Example
fruitName = ["apple", "orange", "banana"]
fruitPrice = (10, 15, 30)
result = zip(fruitName, fruitPrice)
resultList1 = list(result)
resultList2 = list(result)

print(resultList1)
print(resultList2)